from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urljoin, urlparse

import requests  # type: ignore[import-not-found]
from bs4 import BeautifulSoup, NavigableString, Tag  # type: ignore[import-not-found]


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
    for pattern in (
        r"^title:\s*\"(.+?)\"\s*$",
        r"^title:\s*'(.+?)'\s*$",
        r"^title:\s*([^\"'\n][^\n]*?)\s*$",
    ):
        match = re.search(pattern, raw_markdown, flags=re.M)
        if match:
            return match.group(1).strip()
    raise RuntimeError("Could not find Gwern page title in front matter")


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
_HTML_LINK_RE = re.compile(r"<a href=(['\"])(.*?)\\1(?: [^>]*)?>(.*?)</a>")
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
        href = urljoin(base_url, match.group(2))
        label = BeautifulSoup(match.group(3), "html.parser").get_text(" ", strip=True)
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
    # Normalize some Pandoc/Gwern editorial annotations into plain Markdown text.
    line = line.replace(r"[\[", "(")
    line = line.replace(r"\]]{.editorial}", ")")
    line = re.sub(r"\[(.*)\]\{#[^}]+\}", r"\1", line)
    line = re.sub(r"^#\.\s+", "1. ", line)
    line = re.sub(r"\s+\{#[^}]+\}$", "", line)
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
        if "return-to-blog-index-link" in line:
            continue

        title_match = re.fullmatch(r'<div class="admonition-title">(.+)</div>', line)
        if title_match:
            out.append(f"**{title_match.group(1)}**")
            continue

        cleaned = _clean_line(page.url, line)
        if cleaned.strip() == "[[Return to blog index](https://gwern.net/blog/index)]":
            continue
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


def _has_placeholder_front_matter(raw_markdown: str) -> bool:
    return bool(re.search(r"^placeholder:\s*True\s*$", raw_markdown, flags=re.M))


def _annotation_url(page_url: str) -> str:
    parsed = urlparse(page_url)
    page_path = parsed.path
    if not page_path.endswith(".html"):
        page_path += ".html"
    encoded = quote(quote(page_path, safe=""), safe="")
    return f"{parsed.scheme}://{parsed.netloc}/metadata/annotation/{encoded}"


def _normalize_inline_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\u2060", "")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _render_annotation_inline(node: NavigableString | Tag, base_url: str) -> str:
    if isinstance(node, NavigableString):
        return str(node)

    if not isinstance(node, Tag):
        return ""

    name = node.name or ""
    if name == "a":
        href = urljoin(base_url, (node.get("href") or "").strip())
        label = "".join(
            _render_annotation_inline(child, base_url) for child in node.children
        )
        label = _normalize_inline_text(label)
        return f"[{label}]({href})" if href and label else label
    if name in {"em", "i"}:
        inner = _normalize_inline_text(
            "".join(
                _render_annotation_inline(child, base_url) for child in node.children
            )
        )
        return f"*{inner}*" if inner else ""
    if name in {"strong", "b"}:
        inner = _normalize_inline_text(
            "".join(
                _render_annotation_inline(child, base_url) for child in node.children
            )
        )
        return f"**{inner}**" if inner else ""
    if name == "span" and "date-range" in (node.get("class") or []):
        bits: list[str] = []
        sub_text = ""
        for child in node.children:
            if isinstance(child, Tag) and child.name == "sub":
                sub_text = _normalize_inline_text(child.get_text(" ", strip=True))
            else:
                bits.append(_render_annotation_inline(child, base_url))
        main = _normalize_inline_text("".join(bits))
        return f"{main} ({sub_text})" if sub_text else main
    if name == "sub":
        return _normalize_inline_text(node.get_text(" ", strip=True))
    if name == "br":
        return "\n"

    return "".join(
        _render_annotation_inline(child, base_url) for child in node.children
    )


def _render_annotation_paragraph(tag: Tag, base_url: str) -> str:
    return _normalize_inline_text(
        "".join(_render_annotation_inline(child, base_url) for child in tag.children)
    )


def _iter_child_tags(tag: Tag) -> list[Tag]:
    return [child for child in tag.children if isinstance(child, Tag)]


def _render_annotation_list(tag: Tag, base_url: str, indent: str = "") -> list[str]:
    ordered = tag.name == "ol"
    lines: list[str] = []
    items = [
        child for child in tag.children if isinstance(child, Tag) and child.name == "li"
    ]

    for idx, item in enumerate(items, start=1):
        marker = f"{idx}. " if ordered else "- "
        body_prefix = " " * len(marker)
        item_blocks: list[str] = []

        for child in _iter_child_tags(item):
            if child.name in {"ol", "ul"}:
                nested = _render_annotation_list(child, base_url, indent + body_prefix)
                if item_blocks and item_blocks[-1] != "":
                    item_blocks.append("")
                item_blocks.extend(nested)
                continue

            block = _render_annotation_block(child, base_url)
            if not block:
                continue
            if item_blocks and item_blocks[-1] != "":
                item_blocks.append("")
            item_blocks.extend(block)

        if not item_blocks:
            continue

        first, *rest = item_blocks
        lines.append(f"{indent}{marker}{first}")
        for line in rest:
            lines.append(f"{indent}{body_prefix}{line}" if line else "")
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()
    return lines


def _render_annotation_block(tag: Tag, base_url: str) -> list[str]:
    if tag.name == "p":
        paragraph = _render_annotation_paragraph(tag, base_url)
        return [paragraph] if paragraph else []

    if tag.name == "figure":
        lines: list[str] = []
        img = tag.find("img")
        if img is not None and img.get("src"):
            title = _normalize_inline_text(
                (img.get("title") or img.get("alt") or "Image")
            )
            src = urljoin(base_url, img["src"])
            lines.append(f"![{title}]({src})")
        caption = tag.find("figcaption")
        if caption is not None:
            text = _render_annotation_paragraph(caption, base_url)
            if text:
                lines.append(text)
        return lines

    if tag.name == "blockquote":
        lines: list[str] = []
        for child in _iter_child_tags(tag):
            block = _render_annotation_block(child, base_url)
            if not block:
                continue
            for line in block:
                lines.append("> " + line if line else ">")
            lines.append("")
        while lines and lines[-1] == "":
            lines.pop()
        return lines

    if tag.name in {"ol", "ul"}:
        return _render_annotation_list(tag, base_url)

    if tag.name == "div":
        classes = set(tag.get("class") or [])
        if "epigraph" in classes:
            quote = tag.find("blockquote")
            return (
                _render_annotation_block(quote, base_url) if quote is not None else []
            )
        if "similars-append" in classes:
            return []
        if tag.find("hr") is not None:
            return ["---"]

    if tag.name == "hr":
        return ["---"]

    lines: list[str] = []
    for child in _iter_child_tags(tag):
        lines.extend(_render_annotation_block(child, base_url))
    return lines


def _clean_annotation_markdown(page: Page) -> str:
    annotation_html = _fetch(_annotation_url(page.url))
    soup = BeautifulSoup(annotation_html, "html.parser")
    blocks = [tag for tag in soup.contents if isinstance(tag, Tag)]

    author_md = ""
    date_text = ""
    tags_md: list[str] = []
    body_root: Tag | None = None

    for block in blocks:
        author = block.select_one(".author.cite-author a")
        if author is not None:
            author_md = _render_annotation_inline(author, page.url)
            continue

        date = block.select_one(".date.cite-date")
        if date is not None:
            date_text = _normalize_inline_text(date.get_text(" ", strip=True))
            continue

        tag_links = block.select(".link-tags a")
        if tag_links:
            tags_md = [_render_annotation_inline(link, page.url) for link in tag_links]
            continue

        if block.name == "blockquote":
            body_root = block
            break

    if body_root is None:
        raise RuntimeError(f"Could not find rendered annotation body for {page.url}")

    meta_parts = [part for part in [author_md, date_text] if part]
    meta_line = " ".join(meta_parts)
    if tags_md:
        meta_line += (
            f" ({', '.join(tags_md)})" if meta_line else f"({', '.join(tags_md)})"
        )

    body_lines: list[str] = []
    for child in _iter_child_tags(body_root):
        block_lines = _render_annotation_block(child, page.url)
        if not block_lines:
            continue
        body_lines.extend(block_lines)
        body_lines.append("")

    while body_lines and body_lines[-1] == "":
        body_lines.pop()

    parts = [f"# {page.title}", "", f"[{page.title}]({page.url})"]
    if meta_line:
        parts.extend(["", meta_line])
    parts.extend(["", *body_lines, ""])
    return "\n".join(parts)


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
        html_path = html_dir / slug.replace(".md", ".html")
        html_path.write_text(page.raw_html, encoding="utf-8")
        (html_dir / slug).write_text(page.raw_markdown, encoding="utf-8")

        out_path = md_dir / _safe_filename(page.title)
        if _has_placeholder_front_matter(page.raw_markdown):
            annotation_url = _annotation_url(page.url)
            annotation_slug = annotation_url.rsplit("/", 1)[-1]
            (html_dir / annotation_slug).write_text(
                _fetch(annotation_url), encoding="utf-8"
            )
            cleaned = _clean_annotation_markdown(page)
        else:
            cleaned = _clean_markdown(page)
        out_path.write_text(cleaned, encoding="utf-8")
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
