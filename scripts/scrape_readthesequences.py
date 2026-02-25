#!/usr/bin/env python3
"""
Scrape ReadTheseSequences sequence pages into Markdown source files.

This repo's workflow expects:
- Raw source markdown under source/ (gitignored)
- First link under the H1 title is the original link (kept in English)

We fetch each post via the site's built-in `?action=markdown` endpoint to avoid
HTML->Markdown conversion issues.
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


READTHESEQUENCES_HOST = "www.readthesequences.com"


def _http_get(url: str, timeout_s: float = 30.0) -> str:
    req = urllib.request.Request(
        url,
        headers={
            # A real UA reduces the chance of a 403.
            "User-Agent": "agent-translator/1.0 (+https://example.invalid)",
            "Accept": "text/html,text/plain,*/*;q=0.9",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = resp.read()
    # ReadTheseSequences pages are UTF-8.
    return data.decode("utf-8", errors="replace")


class _AnchorExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_a = False
        self._a_href: str | None = None
        self._buf: list[str] = []
        self.anchors: list[tuple[str, str]] = []  # (href, text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = None
        for k, v in attrs:
            if k == "href":
                href = v
                break
        if not href:
            return
        self._in_a = True
        self._a_href = href
        self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag != "a":
            return
        if self._in_a and self._a_href is not None:
            text = "".join(self._buf).strip()
            self.anchors.append((self._a_href, text))
        self._in_a = False
        self._a_href = None
        self._buf = []

    def handle_data(self, data: str) -> None:
        if self._in_a:
            self._buf.append(data)


def _normalize_url(base_url: str, href: str) -> str:
    # Handle protocol-relative and relative URLs.
    return urllib.parse.urljoin(base_url, href)


def _is_post_url(url: str) -> bool:
    """
    ReadTheseSequences posts look like:
      https://www.readthesequences.com/The-Parable-Of-The-Dagger
    We exclude sequence pages and navigation pages.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    if parsed.netloc != READTHESEQUENCES_HOST:
        return False
    path = parsed.path.strip("/")
    if not path:
        return False
    # Exclude sequence pages.
    if path.endswith("-Sequence"):
        return False
    # Exclude obvious site pages.
    if path in {"", "index", "rss"}:
        return False
    # Exclude query-only variants.
    if parsed.query:
        return False
    return True


def _slug_from_post_url(post_url: str) -> str:
    return urllib.parse.urlparse(post_url).path.strip("/").split("/")[-1]


_REF_DEF_RE = re.compile(
    r"^\s*\[(?P<id>[^\]]+)\]:\s+(?P<url>\S+)(?:\s+\"[^\"]*\")?\s*$"
)
_REF_USE_RE = re.compile(r"\[(?P<text>[^\]]+)\]\[(?P<id>[^\]]+)\]")


def _convert_reference_links(md: str) -> str:
    """
    Convert reference-style links:
      [text][8]
      ...
      [8]: https://example.com
    into inline links:
      [text](https://example.com)

    Keeps lines intact (does not reflow paragraphs).
    """
    lines = md.splitlines()
    ref_map: dict[str, str] = {}
    keep_lines: list[str] = []
    for line in lines:
        m = _REF_DEF_RE.match(line)
        if m:
            ref_id = m.group("id").strip()
            ref_url = m.group("url").strip()
            # Drop surrounding <> if any.
            if ref_url.startswith("<") and ref_url.endswith(">"):
                ref_url = ref_url[1:-1]
            ref_map[ref_id] = ref_url
            continue
        keep_lines.append(line)

    def repl(match: re.Match[str]) -> str:
        text = match.group("text")
        ref_id = match.group("id")
        url = ref_map.get(ref_id)
        if not url:
            return match.group(0)
        return f"[{text}]({url})"

    out_lines = []
    for line in keep_lines:
        out_lines.append(_REF_USE_RE.sub(repl, line))
    return "\n".join(out_lines)


def _sanitize_filename(name: str) -> str:
    # Keep ASCII; replace problematic path characters.
    name = name.strip()
    name = re.sub(r"[\\/:*?\"<>|]", "-", name)
    name = re.sub(r"\\s+", " ", name)
    return name


@dataclass(frozen=True)
class Post:
    idx: int
    url: str
    slug: str
    title: str
    markdown: str


def _fetch_post_markdown(post_url: str) -> str:
    # Fetch built-in Markdown view.
    md_url = post_url + "?action=markdown"
    return _http_get(md_url)


def _extract_title_from_markdown(md: str, fallback: str) -> tuple[str, str]:
    """
    Returns (title, md_without_title_line_if_present).
    """
    lines = md.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        return title, "\n".join(lines[1:]).lstrip("\n")
    return fallback, md


def _clean_readthesequences_markdown(md_body: str, title: str) -> str:
    """
    The `?action=markdown` output includes site chrome (Source/Markdown/Talk and
    Home/About/Search/Contents) and often repeats the H1 title.
    Strip those so `source/` contains only content.
    """
    out: list[str] = []
    for line in md_body.splitlines():
        s = line.strip()
        # Strip the site chrome lines.
        if "action=source" in line and "action=markdown" in line:
            continue
        if (
            s.startswith("[Home](")
            and "readthesequences.com" in s
            and "[Contents](" in s
        ):
            continue
        # Strip bottom navigation / star icon.
        if "star.svg" in line:
            continue
        if s.startswith("[Top](") and "readthesequences.com/Contents" in s:
            continue
        if s.startswith("[Book](") and "readthesequences.com/Book" in s:
            continue
        if s.startswith("[Sequence](") and "readthesequences.com/" in s:
            continue
        # The markdown export appends sequence navigation; drop everything after it.
        if s.startswith("[A Human"):
            break
        # Drop duplicated H1 that matches the extracted title.
        if s == f"# {title}":
            continue
        out.append(line)

    # Trim trailing prev/next navigation links that the export sometimes appends.
    # These typically use non-hyphenated slugs like /TheParableOfTheDagger.
    def is_trailing_nav_link(line: str) -> bool:
        s2 = line.strip()
        m = re.fullmatch(
            r"\[[^\]]+\]\((https?://www\.readthesequences\.com/[^)#?]+)\)\s*", s2
        )
        if not m:
            return False
        path = urllib.parse.urlparse(m.group(1)).path.strip("/")
        if not path:
            return False
        if "-" in path:
            return False
        if path.endswith("Sequence"):
            return False
        if path in {"HomePage", "About", "Search", "Contents"}:
            return False
        return True

    # Remove blank lines at EOF.
    while out and not out[-1].strip():
        out.pop()
    # Remove one or more trailing nav links.
    while out and is_trailing_nav_link(out[-1]):
        out.pop()
        while out and not out[-1].strip():
            out.pop()

    # Trim leading/trailing blank lines.
    cleaned = "\n".join(out).strip("\n")
    return cleaned


def scrape_sequence(sequence_url: str) -> list[str]:
    """
    Return ordered list of post URLs in the sequence page.
    """
    html_text = _http_get(sequence_url)
    # The sequence page has a single ordered list (<ol>...</ol>) containing the
    # actual sequence entries. Restrict parsing to that region so we don't pick
    # up top nav / bottom nav links.
    ol_start = html_text.find("<ol")
    ol_end = html_text.find("</ol>")
    region = html_text
    if ol_start != -1 and ol_end != -1 and ol_end > ol_start:
        region = html_text[ol_start : ol_end + len("</ol>")]

    parser = _AnchorExtractor()
    parser.feed(region)

    # Keep anchor order as they appear in the sequence page.
    seen: set[str] = set()
    posts: list[str] = []
    for href, text in parser.anchors:
        t = re.sub(r"\s+", " ", text).strip()
        if not t:
            continue
        url = _normalize_url(sequence_url, href)
        if not _is_post_url(url):
            continue
        if url in seen:
            continue
        seen.add(url)
        posts.append(url)
    return posts


def build_posts(post_urls: Iterable[str], sleep_s: float = 0.0) -> list[Post]:
    posts: list[Post] = []
    for i, url in enumerate(post_urls, start=1):
        slug = _slug_from_post_url(url)
        md_raw = _fetch_post_markdown(url)
        title, md_body = _extract_title_from_markdown(
            md_raw, fallback=slug.replace("-", " ")
        )
        md_body = _convert_reference_links(md_body)
        md_body = _clean_readthesequences_markdown(md_body, title=title)

        # Ensure the "original link" is the first link under the title.
        md_final = "\n".join(
            [
                f"# {title}",
                "",
                f"[{title}]({url})",
                "",
                md_body.strip("\n"),
                "",
            ]
        )
        posts.append(Post(idx=i, url=url, slug=slug, title=title, markdown=md_final))
        if sleep_s:
            time.sleep(sleep_s)
    return posts


def write_posts(posts: list[Post], out_dir: Path, prefix_width: int = 2) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for p in posts:
        prefix = str(p.idx).zfill(prefix_width)
        filename = f"{prefix} {p.title}.md"
        filename = _sanitize_filename(filename)
        path = out_dir / filename
        path.write_text(p.markdown, encoding="utf-8")
        written.append(path)
    return written


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sequence-url", required=True)
    ap.add_argument("--out-source", default="source")
    ap.add_argument("--sleep", type=float, default=0.0)
    ap.add_argument("--prefix-width", type=int, default=2)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sequence_url = args.sequence_url.strip()
    post_urls = scrape_sequence(sequence_url)
    if args.dry_run:
        for u in post_urls:
            print(u)
        return 0

    posts = build_posts(post_urls, sleep_s=args.sleep)
    written = write_posts(posts, Path(args.out_source), prefix_width=args.prefix_width)
    print(f"Wrote {len(written)} files to {args.out_source}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
