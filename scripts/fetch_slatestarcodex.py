from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests  # type: ignore[import-not-found]
from bs4 import BeautifulSoup, NavigableString, Tag  # type: ignore[import-not-found]


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    author_name: str
    author_url: str
    date_text: str
    body_lines: list[str]
    raw_html: str


def _fetch(url: str) -> str:
    resp = requests.get(
        url,
        headers={"User-Agent": "agent-translator (+https://slatestarcodex.com/)"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.text


def _clean_text(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = text.replace("\u2060", "")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _article_slug(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    slug = Path(path).name or "article"
    return f"{slug}.html"


def _render_inline(node: NavigableString | Tag, base_url: str) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    if node.name == "a":
        href = urljoin(base_url, (node.get("href") or "").strip())
        label = _clean_text(
            "".join(_render_inline(child, base_url) for child in node.children)
        )
        return f"[{label}]({href})" if href and label else label

    if node.name in {"i", "em"}:
        text = _clean_text(
            "".join(_render_inline(child, base_url) for child in node.children)
        )
        return f"*{text}*" if text else ""

    if node.name in {"b", "strong"}:
        text = _clean_text(
            "".join(_render_inline(child, base_url) for child in node.children)
        )
        return f"**{text}**" if text else ""

    if node.name == "br":
        return "\n"

    return "".join(_render_inline(child, base_url) for child in node.children)


def _render_paragraph(tag: Tag, base_url: str) -> str:
    text = "".join(_render_inline(child, base_url) for child in tag.children)
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    text = text.replace(" :", ":")
    text = text.replace(" ;", ";")
    text = text.replace(" ?", "?")
    text = text.replace(" !", "!")
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\[\s+", "[", text)
    text = re.sub(r"\s+\]", "]", text)
    return _clean_text(text)


def _extract_article(url: str, raw_html: str) -> Article:
    soup = BeautifulSoup(raw_html, "html.parser")
    post = soup.select_one("div.post")
    if post is None:
        raise RuntimeError("Could not locate Slate Star Codex post container")

    title_tag = post.select_one("h1.pjgm-posttitle")
    if title_tag is None:
        raise RuntimeError("Could not locate post title")
    title = _clean_text(title_tag.get_text(" ", strip=True))

    author_tag = post.select_one(".author.vcard a")
    author_name = (
        _clean_text(author_tag.get_text(" ", strip=True)) if author_tag else ""
    )
    author_url = (
        urljoin(url, (author_tag.get("href") or "").strip()) if author_tag else ""
    )

    date_tag = post.select_one(".entry-date")
    date_text = _clean_text(date_tag.get_text(" ", strip=True)) if date_tag else ""

    body = post.select_one("div.pjgm-postcontent")
    if body is None:
        raise RuntimeError("Could not locate post body")

    body_lines: list[str] = []
    for tag in body.find_all("p", recursive=False):
        text = _render_paragraph(tag, url)
        if not text:
            continue
        body_lines.extend([text, ""])

    while body_lines and not body_lines[-1].strip():
        body_lines.pop()

    return Article(
        title=title,
        url=url,
        author_name=author_name,
        author_url=author_url,
        date_text=date_text,
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

    if article.author_name:
        author_md = (
            f"[{article.author_name}]({article.author_url})"
            if article.author_url
            else article.author_name
        )
        byline = author_md
        if article.date_text:
            byline = f"{byline} {article.date_text}"
        parts += ["", byline]
    elif article.date_text:
        parts += ["", article.date_text]

    parts += ["", *article.body_lines, ""]
    out_path.write_text("\n".join(parts), encoding="utf-8")


def fetch_all(urls: list[str], html_dir: Path, md_dir: Path) -> list[Path]:
    html_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for url in urls:
        raw_html = _fetch(url)
        article = _extract_article(url, raw_html)

        (html_dir / _article_slug(url)).write_text(raw_html, encoding="utf-8")

        out_path = md_dir / _sanitize_filename(article.title)
        _write_markdown(out_path, article)
        written.append(out_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--html-dir", default="html/slatestarcodex")
    parser.add_argument("--md-dir", default="source")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    for path in fetch_all(
        args.urls, repo_root / args.html_dir, repo_root / args.md_dir
    ):
        print(path)


if __name__ == "__main__":
    main()
