from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import requests  # type: ignore[import-not-found]
from bs4 import BeautifulSoup, NavigableString, Tag  # type: ignore[import-not-found]


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    byline: str
    body_lines: list[str]
    raw_html: str


def _fetch(url: str) -> str:
    resp = requests.get(
        url,
        headers={"User-Agent": "agent-translator (+https://naturalchild.org/)"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.text


def _clean_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _render_inline(node: Tag) -> str:
    parts: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue
        if not isinstance(child, Tag):
            continue
        if child.name == "a":
            href = (child.get("href") or "").strip()
            label = _clean_text(child.get_text(" ", strip=True))
            if href and label:
                parts.append(f"[{label}]({href})")
                continue
        if child.name in {"i", "em"}:
            text = _clean_text(child.get_text(" ", strip=True))
            if text:
                parts.append(f"*{text}*")
                continue
        if child.name == "sup":
            text = _clean_text(child.get_text(" ", strip=True))
            if text:
                parts.append(f"^{text}")
                continue
        parts.append(_clean_text(child.get_text(" ", strip=True)))
    return _clean_text("".join(parts))


def _article_slug(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    return Path(path).name or "article"


def _extract_article(url: str, raw_html: str) -> Article:
    soup = BeautifulSoup(raw_html, "html.parser")
    h1 = soup.find("h1")
    if h1 is None:
        raise RuntimeError("Could not locate article title")

    title = _clean_text(h1.get_text(" ", strip=True))
    byline_tag = h1.find_next("div", class_="byline")
    byline = _clean_text(byline_tag.get_text(" ", strip=True)) if byline_tag else ""

    body_lines: list[str] = []
    footnote_text = ""

    for tag in h1.find_all_next():
        if not isinstance(tag, Tag):
            continue
        if tag == h1:
            continue
        if tag.name == "h1":
            break
        if tag.name == "div":
            if "byline" in (tag.get("class") or []):
                continue
            continue
        if tag.name not in {"h2", "p"}:
            continue

        plain_text = _clean_text(tag.get_text(" ", strip=True))
        text = _render_inline(tag)
        if not text:
            continue

        if text == "Anecdote footnote written by Jan Hunt.":
            break
        if re.match(r"^\^?1\s*Once when\b", plain_text):
            footnote_text = re.sub(r"^\^?1\s*", "", plain_text).strip()
            continue

        if tag.name == "h2":
            body_lines.extend([f"## {text}", ""])
            continue

        if text == "What about the parent who works outside of the home?":
            body_lines.extend([f"## {text}", ""])
            continue

        if plain_text in {"None. 1", "None. ^1"} or text in {"None.^1", "None. ^1"}:
            body_lines.extend(["None.^[FOOTNOTE_PLACEHOLDER]", ""])
            continue

        body_lines.extend([text, ""])

    if footnote_text:
        body_lines = [
            line.replace("^[FOOTNOTE_PLACEHOLDER]", f"^[{footnote_text}]")
            for line in body_lines
        ]

    while body_lines and not body_lines[-1].strip():
        body_lines.pop()

    return Article(
        title=title,
        url=url,
        byline=byline,
        body_lines=body_lines,
        raw_html=raw_html,
    )


def _sanitize_filename(title: str) -> str:
    cleaned = title
    for ch in '/\\:*?"<>|':
        cleaned = cleaned.replace(ch, "-")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return f"{cleaned}.md"


def _write_markdown(out_path: Path, article: Article) -> None:
    parts = [f"# {article.title}", "", f"[{article.title}]({article.url})"]
    if article.byline:
        parts += ["", article.byline]
    parts += ["", *article.body_lines, ""]
    out_path.write_text("\n".join(parts), encoding="utf-8")


def fetch_all(urls: list[str], html_dir: Path, md_dir: Path) -> list[Path]:
    html_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for url in urls:
        raw_html = _fetch(url)
        article = _extract_article(url, raw_html)
        slug = _article_slug(url)
        (html_dir / slug).write_text(raw_html, encoding="utf-8")
        out_path = md_dir / _sanitize_filename(article.title)
        _write_markdown(out_path, article)
        written.append(out_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--html-dir", default="html/naturalchild")
    parser.add_argument("--md-dir", default="source")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    for path in fetch_all(
        args.urls, repo_root / args.html_dir, repo_root / args.md_dir
    ):
        print(path)


if __name__ == "__main__":
    main()
