from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urljoin

import requests  # type: ignore[import-not-found]
from bs4 import BeautifulSoup  # type: ignore[import-not-found]


@dataclass(frozen=True)
class Page:
    title: str
    url: str
    markdown_url: str
    raw_html: str
    raw_markdown: str


def _fetch(url: str) -> str:
    resp = requests.get(
        url,
        headers={
            "User-Agent": "agent-translator (+https://gwern.net/; educational use)"
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.text


def _discover_markdown_url(url: str, raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, "html.parser")
    for link in soup.find_all("link", href=True):
        if link.get("type") == "text/markdown":
            return urljoin(url, link["href"])
    raise RuntimeError(f"Could not find markdown source link for {url}")


def _discover_title(raw_markdown: str) -> str:
    match = re.search(r'^title:\s*"(.+?)"\s*$', raw_markdown, flags=re.M)
    if not match:
        raise RuntimeError("Could not find Gwern page title in front matter")
    return match.group(1)


def _load_page(url: str) -> Page:
    raw_html = _fetch(url)
    markdown_url = _discover_markdown_url(url, raw_html)
    raw_markdown = _fetch(markdown_url)
    title = _discover_title(raw_markdown)
    return Page(
        title=title,
        url=url,
        markdown_url=markdown_url,
        raw_html=raw_html,
        raw_markdown=raw_markdown,
    )


_FRONT_MATTER_RE = re.compile(r"^---\n.*?\n\.\.\.\n", flags=re.S)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->")
_HTML_LINK_RE = re.compile(r'<a href="([^"]+)"(?: [^>]*)?>(.*?)</a>')
_SPAN_ID_RE = re.compile(r'<span id="[^"]*"></span>')
_MARGINNOTE_RE = re.compile(r"\[([^\]]+)\]\{\.marginnote(?: [^}]*)?\}")
_WIKI_LINK_RE = re.compile(r"(?<![\\^])\[([^\]]+)\]\(!W(?: \"([^\"]+)\")?\)")
_INFLATION_RE = re.compile(r"(?<![\\^])\[([^\]]+)\]\(\$(\d{4})\)([mbt]?)")
_LINK_TITLE_RE = re.compile(r'(\]\((?:[^()\s]|\\.)+?)\s+"[^"]*"\)')
_IMG_TITLE_RE = re.compile(r'(!\[[^\]]*\]\((?:[^()\s]|\\.)+?)\s+"[^"]*"\)')
_LINK_ATTR_RE = re.compile(r"(\]\((?:[^()\s]|\\.)+\))\{[^}]+\}")
_IMAGE_ATTR_RE = re.compile(r"(!\[[^\]]*\]\((?:[^()\s]|\\.)+\))\{[^}]+\}")
_RAW_DIV_RE = re.compile(r"</?div(?: [^>]*)?>")


def _html_link_to_markdown(base_url: str, text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        href = urljoin(base_url, match.group(1))
        label = BeautifulSoup(match.group(2), "html.parser").get_text(" ", strip=True)
        return f"[{label}]({href})"

    return _HTML_LINK_RE.sub(repl, text)


def _rewrite_relative_markdown_urls(base_url: str, text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        raw_url = match.group(2)
        if raw_url.startswith(("#", "mailto:", "http://", "https://")):
            return match.group(0)
        return f"{match.group(1)}{urljoin(base_url, raw_url)}{match.group(3)}"

    # Match Markdown links/images while keeping optional titles already stripped later.
    return re.sub(
        r"(!?\[[^\]]*\]\()([^)\s]+)([^)]*\))",
        repl,
        text,
    )


def _rewrite_trailing_image_url(base_url: str, text: str) -> str:
    return re.sub(
        r"(!\[.*\]\()(/[^)\s]+)(\))$",
        lambda match: f"{match.group(1)}{urljoin(base_url, match.group(2))}{match.group(3)}",
        text,
    )


def _rewrite_wikipedia_shorthand(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2) or label
        slug = quote(target.replace(" ", "_"), safe="()':,._-")
        return f"[{label}](https://en.wikipedia.org/wiki/{slug})"

    return _WIKI_LINK_RE.sub(repl, text)


def _rewrite_inflation_shorthand(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        amount = match.group(1)
        year = match.group(2)
        suffix = match.group(3)
        return f"{amount}{suffix} ({year} dollars)"

    return _INFLATION_RE.sub(repl, text)


def _clean_line(base_url: str, line: str) -> str:
    line = html.unescape(line)
    line = line.replace("\u2009", " ")
    line = _HTML_COMMENT_RE.sub("", line)
    line = _SPAN_ID_RE.sub("", line)
    line = _RAW_DIV_RE.sub("", line)
    line = _html_link_to_markdown(base_url, line)
    line = _rewrite_wikipedia_shorthand(line)
    line = _rewrite_inflation_shorthand(line)
    line = _MARGINNOTE_RE.sub(r"**\1**", line)
    line = _LINK_TITLE_RE.sub(r"\1)", line)
    line = _IMG_TITLE_RE.sub(r"\1)", line)
    line = _LINK_ATTR_RE.sub(r"\1", line)
    line = _IMAGE_ATTR_RE.sub(r"\1", line)
    line = _rewrite_relative_markdown_urls(base_url, line)
    line = _rewrite_trailing_image_url(base_url, line)
    return line.rstrip()


def _clean_markdown(page: Page) -> str:
    body = _FRONT_MATTER_RE.sub("", page.raw_markdown, count=1)
    out: list[str] = []
    in_comment = False

    for raw_line in body.splitlines():
        line = raw_line.rstrip("\n")

        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if "<!--" in line:
            if "-->" not in line:
                in_comment = True
            continue
        if "{.display-not}" in line:
            continue
        if line == '<div class="abstract">':
            continue
        if line == '<div class="epigraph">':
            continue
        if line == '<div class="interview">':
            continue
        if line == '<div class="admonition note">':
            continue
        if line == "</div>":
            continue

        title_match = re.fullmatch(r'<div class="admonition-title">(.+)</div>', line)
        if title_match:
            out.append(f"**{title_match.group(1)}**")
            continue

        cleaned = _clean_line(page.url, line)
        out.append(cleaned)

    # Trim surrounding blank lines and squeeze repeated empties.
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()

    squeezed: list[str] = []
    blank_run = 0
    for line in out:
        if not line.strip():
            blank_run += 1
            if blank_run > 1:
                continue
        else:
            blank_run = 0
        squeezed.append(line)

    body_md = "\n".join(squeezed).rstrip() + "\n"
    return f"# {page.title}\n\n[{page.title}]({page.url})\n\n{body_md}"


def _safe_filename(title: str) -> str:
    cleaned = title
    for ch in '/\\:*?"<>|':
        cleaned = cleaned.replace(ch, "-")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return f"{cleaned}.md"


def fetch_all(urls: list[str], html_dir: Path, md_dir: Path) -> list[Path]:
    html_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for url in urls:
        page = _load_page(url)
        slug = page.markdown_url.rsplit("/", 1)[-1]
        (html_dir / slug.replace(".md", ".html")).write_text(
            page.raw_html, encoding="utf-8"
        )
        (html_dir / slug).write_text(page.raw_markdown, encoding="utf-8")

        out_path = md_dir / _safe_filename(page.title)
        out_path.write_text(_clean_markdown(page), encoding="utf-8")
        written.append(out_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--html-dir", default="html/gwern")
    parser.add_argument("--md-dir", default="source")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    for path in fetch_all(
        args.urls, repo_root / args.html_dir, repo_root / args.md_dir
    ):
        print(path)


if __name__ == "__main__":
    main()
