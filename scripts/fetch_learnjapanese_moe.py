from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin


@dataclass(frozen=True)
class Page:
    title: str
    url: str
    slug: str


PAGES: list[Page] = [
    Page("Japanese Guide", "https://learnjapanese.moe/guide/", "guide"),
    Page("30 Day Japanese", "https://learnjapanese.moe/routine/", "routine"),
    Page("The Shoui Method", "https://learnjapanese.moe/shouimethod/", "shouimethod"),
    Page("Speaking Japanese", "https://learnjapanese.moe/speaking/", "speaking"),
    Page("Anime Japanese", "https://learnjapanese.moe/animejp/", "animejp"),
    Page("Learning Kanji", "https://learnjapanese.moe/kanji/", "kanji"),
    Page(
        "Reading Techniques and Strategies",
        "https://learnjapanese.moe/readingtips/",
        "readingtips",
    ),
    Page("Monolingual Guide", "https://learnjapanese.moe/monolingual/", "monolingual"),
    Page("Japanese FAQ", "https://learnjapanese.moe/faq/", "faq"),
    Page("Fixing your font", "https://learnjapanese.moe/font/", "font"),
    Page("How to use 5ch", "https://learnjapanese.moe/2ch/", "2ch"),
    Page("Japanese typing", "https://learnjapanese.moe/ime/", "ime"),
]


def _rewrite_relative_urls(soup, base_url: str) -> None:
    for a in soup.find_all("a", href=True):
        a["href"] = urljoin(base_url, a["href"])
    for img in soup.find_all("img", src=True):
        img["src"] = urljoin(base_url, img["src"])


def _simplify_html(soup) -> None:
    # MkDocs Material adds "permalink" anchors (e.g. "¶") inside headings.
    for a in soup.find_all("a", class_="headerlink"):
        a.decompose()

    # Strip styling/layout noise so Pandoc emits real Markdown instead of raw HTML.
    for img in soup.find_all("img"):
        if (img.get("src") or "").startswith("data:"):
            img.decompose()

    for a in soup.find_all("a"):
        classes = set(a.get("class", []) or [])
        if "md-button" in classes:
            # Convert Material "button" links into plain links.
            for img in a.find_all("img"):
                img.decompose()
            href = a.get("href")
            text = a.get_text(" ", strip=True)
            a.attrs = {}
            if href:
                a["href"] = href
            a.string = text

    for img in soup.find_all("img"):
        src = img.get("src")
        alt = img.get("alt")
        img.attrs = {}
        if src:
            img["src"] = src
        if alt:
            img["alt"] = alt

    for tag in soup.find_all(["div", "span"]):
        tag.unwrap()


def _extract_article_html(html: str, base_url: str) -> str:
    # Avoid full mkdocs chrome; keep only the page content.
    from bs4 import BeautifulSoup  # type: ignore[import-not-found]

    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", class_="md-content__inner")
    if article is None:
        # Fallback: keep the document body.
        article = soup.body or soup

    _rewrite_relative_urls(article, base_url)
    _simplify_html(article)

    h1 = article.find("h1")
    if h1 is not None:
        h1.decompose()

    return str(article)


def _pandoc_html_to_md(html: str) -> str:
    # Keep paragraphs as single lines to make line-by-line translation easier.
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "pandoc failed")
    md = proc.stdout.rstrip() + "\n"

    # Normalize leftover inline HTML from mkdocs keyboard key markup.
    md = md.replace("</span><span", "</span>+<span")
    md = md.replace("</kbd><kbd", "</kbd>+<kbd")

    import re

    md = re.sub(r'<span class="kbd[^"]*">([^<]+)</span>', r"`\1`", md)
    md = re.sub(r"<kbd[^>]*>([^<]+)</kbd>", r"`\1`", md)

    # Best-effort cleanup if any stray span tags remain.
    md = re.sub(r"</?span[^>]*>", "", md)
    return md


def _write_markdown(out_path: Path, title: str, url: str, body_md: str) -> None:
    # First link under the title is the original link (kept as-is for translators).
    content = f"# {title}\n\n[{title}]({url})\n\n{body_md}"
    out_path.write_text(content, encoding="utf-8")


def _ensure_dirs(*paths: Path) -> None:
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)


def _fetch(url: str) -> str:
    import requests  # type: ignore[import-not-found]

    resp = requests.get(
        url,
        headers={
            "User-Agent": "agent-translator (+https://learnjapanese.moe/; educational use)"
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.text


def fetch_all(pages: Iterable[Page], html_dir: Path, md_dir: Path) -> None:
    _ensure_dirs(html_dir, md_dir)
    for page in pages:
        raw_html = _fetch(page.url)
        (html_dir / f"{page.title}.html").write_text(raw_html, encoding="utf-8")

        article_html = _extract_article_html(raw_html, page.url)
        body_md = _pandoc_html_to_md(article_html)
        _write_markdown(md_dir / f"{page.title}.md", page.title, page.url, body_md)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    fetch_all(PAGES, repo_root / "html", repo_root / "source")


if __name__ == "__main__":
    main()
