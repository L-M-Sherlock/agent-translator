from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests  # type: ignore[import-not-found]
from bs4 import BeautifulSoup, Tag  # type: ignore[import-not-found]


@dataclass(frozen=True)
class Post:
    title: str
    url: str
    subtitle: str
    author_name: str
    author_handle: str
    date_text: str
    slug: str
    raw_html: str
    body_html: str


def _fetch(url: str) -> str:
    resp = requests.get(
        url,
        headers={
            "User-Agent": "agent-translator (+https://substack.com/; educational use)"
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.text


def _extract_preloads(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script"):
        text = script.string or script.get_text()
        if "window._preloads" not in text or "JSON.parse(" not in text:
            continue
        match = re.search(
            r'window\._preloads\s*=\s*JSON\.parse\((".*")\)\s*$',
            text,
            re.S,
        )
        if not match:
            continue
        return json.loads(json.loads(match.group(1)))
    raise RuntimeError("Could not locate Substack preload data")


def _pick_author_name(preloads: dict) -> str:
    post = preloads.get("post", {})
    for key in ("publishedBylines", "bylines"):
        bylines = post.get(key) or []
        if bylines:
            byline = bylines[0] or {}
            name = (byline.get("name") or "").strip()
            if name:
                return name
    pub = preloads.get("pub", {})
    return (pub.get("copyright") or "").strip() or "Unknown Author"


def _author_handle(url: str) -> str:
    host = urlparse(url).hostname or ""
    return host.split(".")[0]


def _format_date(post_date: str) -> str:
    dt = datetime.fromisoformat(post_date.replace("Z", "+00:00"))
    return dt.astimezone(timezone.utc).strftime("%b %d, %Y")


def _normalize_heading_text(node: Tag) -> None:
    text = " ".join(node.stripped_strings)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    node.clear()
    node.append(text)


def _is_signature_paragraph(node: object) -> bool:
    return (
        isinstance(node, Tag)
        and node.name == "p"
        and node.get_text(" ", strip=True) in {"Peter", "Peter Gray"}
    )


def _is_button_wrapper(node: object) -> bool:
    return (
        isinstance(node, Tag)
        and node.name == "p"
        and "button-wrapper" in (node.get("class") or [])
    )


def _is_subscription_blurb(node: object) -> bool:
    if not isinstance(node, Tag) or node.name != "p":
        return False
    text = node.get_text(" ", strip=True)
    return (
        text.startswith("Thank you for reading this letter. Subscribe now")
        or text.startswith("Thanks for reading")
        or text.startswith("If you haven’t yet subscribed to this Substack series")
        or text.startswith("If you haven't yet subscribed to this Substack series")
        or text.startswith("If you haven’t yet subscribed to this Substack")
        or text.startswith("If you haven't yet subscribed to this Substack")
    )


def _clean_body_html(body_html: str) -> str:
    soup = BeautifulSoup(body_html, "html.parser")

    for node in list(soup.find_all()):
        if _is_button_wrapper(node) or _is_subscription_blurb(node):
            node.decompose()

    for node in list(soup.find_all("div", class_="captioned-button-wrap")):
        node.decompose()

    for node in list(soup.find_all("div", class_="captioned-image-container")):
        prev = node.find_previous_sibling()
        nxt = node.find_next_sibling()
        if _is_signature_paragraph(prev) or _is_button_wrapper(nxt):
            node.decompose()

    for node in soup.find_all(["sup", "sub"]):
        node.unwrap()

    for img in soup.find_all("img"):
        src = img.get("src")
        alt = img.get("alt")
        if src and src.startswith("data:"):
            img.decompose()
            continue
        img.attrs = {}
        if src:
            img["src"] = src
        if alt:
            img["alt"] = alt

    for node in soup.find_all(re.compile(r"^h[1-6]$")):
        _normalize_heading_text(node)

    for node in soup.find_all("p"):
        if node.get_text(strip=True) == "----":
            node.name = "hr"
            node.clear()

    for node in soup.find_all(["div", "figure", "span"]):
        node.unwrap()

    for node in list(soup.find_all("p")):
        if not node.get_text(strip=True) and not node.find(True):
            node.decompose()

    return str(soup)


def _pandoc_html_to_md(html: str) -> str:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required")
    proc = subprocess.run(
        [pandoc, "--from=html", "--to=gfm", "--wrap=none"],
        input=html,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "pandoc failed")
    md = proc.stdout.replace("\u00a0", " ")
    kept_lines: list[str] = []
    for line in md.splitlines():
        stripped = line.strip()
        if "data:image" in stripped:
            continue
        kept_lines.append(line)
    md = "\n".join(kept_lines)
    md = re.sub(r"(?m)^-{20,}$", "---", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


def _sanitize_filename(title: str) -> str:
    cleaned = title
    for ch in '/\\:*?"<>|':
        cleaned = cleaned.replace(ch, "-")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return f"{cleaned}.md"


def _load_post(url: str) -> Post:
    raw_html = _fetch(url)
    preloads = _extract_preloads(raw_html)
    post = preloads["post"]
    return Post(
        title=post["title"].strip(),
        url=post["canonical_url"],
        subtitle=(post.get("subtitle") or "").strip(),
        author_name=_pick_author_name(preloads),
        author_handle=_author_handle(url),
        date_text=_format_date(post["post_date"]),
        slug=post["slug"],
        raw_html=raw_html,
        body_html=_clean_body_html(post["body_html"]),
    )


def _write_markdown(out_path: Path, post: Post, body_md: str) -> None:
    parts = [f"# {post.title}", "", f"[{post.title}]({post.url})"]
    if post.subtitle:
        parts += ["", f"### {post.subtitle}"]
    if post.author_name:
        parts += [
            "",
            f"[{post.author_name}](https://substack.com/@{post.author_handle})",
        ]
    parts += ["", post.date_text, "", body_md.rstrip(), ""]
    content = "\n".join(parts)
    cleaned_lines: list[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if "data:image" in stripped:
            continue
        cleaned_lines.append(line)
    content = re.sub(r"\n{3,}", "\n\n", "\n".join(cleaned_lines)).strip() + "\n"
    out_path.write_text(content, encoding="utf-8")


def fetch_all(urls: list[str], html_dir: Path, md_dir: Path) -> list[Path]:
    html_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for url in urls:
        post = _load_post(url)
        body_md = _pandoc_html_to_md(post.body_html)
        html_path = html_dir / f"{post.slug}.html"
        md_path = md_dir / _sanitize_filename(post.title)
        html_path.write_text(post.raw_html, encoding="utf-8")
        _write_markdown(md_path, post, body_md)
        written.append(md_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--html-dir", default="html/substack")
    parser.add_argument("--md-dir", default="source")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    written = fetch_all(
        args.urls,
        repo_root / args.html_dir,
        repo_root / args.md_dir,
    )
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
