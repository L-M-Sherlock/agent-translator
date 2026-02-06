from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class Page:
    title: str
    url: str
    slug: str


SEQUENCE_URL = "https://www.readthesequences.com/Fragile-Purposes-Sequence"

# The user requested these specific articles under the sequence.
PAGES: list[Page] = [
    Page(
        "Belief in Intelligence",
        "https://www.readthesequences.com/Belief-In-Intelligence",
        "Belief-In-Intelligence",
    ),
    Page(
        "Humans in Funny Suits",
        "https://www.readthesequences.com/Humans-In-Funny-Suits",
        "Humans-In-Funny-Suits",
    ),
    Page(
        "Optimization and the Intelligence Explosion",
        "https://www.readthesequences.com/Optimization-And-The-Intelligence-Explosion",
        "Optimization-And-The-Intelligence-Explosion",
    ),
    Page(
        "Ghosts in the Machine",
        "https://www.readthesequences.com/Ghosts-In-The-Machine",
        "Ghosts-In-The-Machine",
    ),
    Page(
        "Artificial Addition",
        "https://www.readthesequences.com/Artificial-Addition",
        "Artificial-Addition",
    ),
    Page(
        "Terminal Values and Instrumental Values",
        "https://www.readthesequences.com/Terminal-Values-And-Instrumental-Values",
        "Terminal-Values-And-Instrumental-Values",
    ),
    Page(
        "Leaky Generalizations",
        "https://www.readthesequences.com/Leaky-Generalizations",
        "Leaky-Generalizations",
    ),
    Page(
        "The Hidden Complexity of Wishes",
        "https://www.readthesequences.com/The-Hidden-Complexity-Of-Wishes",
        "The-Hidden-Complexity-Of-Wishes",
    ),
    Page(
        "Anthropomorphic Optimism",
        "https://www.readthesequences.com/Anthropomorphic-Optimism",
        "Anthropomorphic-Optimism",
    ),
    Page(
        "Lost Purposes",
        "https://www.readthesequences.com/Lost-Purposes",
        "Lost-Purposes",
    ),
]


def _ensure_dirs(*paths: Path) -> None:
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)


def _fetch(url: str) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "agent-translator (+https://www.readthesequences.com/; educational use)",
        },
    )
    with urlopen(req, timeout=60) as resp:
        data = resp.read()
    # Site uses UTF-8.
    return data.decode("utf-8")


def _strip_site_chrome(md: str, title: str) -> str:
    """
    readthesequences.com supports ?action=markdown but includes navigation links
    and duplicate headings. Remove those so translators get the article text.
    """
    lines = [ln.rstrip() for ln in md.splitlines()]

    out: list[str] = []
    for ln in lines:
        s = ln.strip()
        if not s:
            # Keep blank lines (Pandoc and translators rely on them).
            out.append("")
            continue

        # Drop the nav block inserted by the site.
        if "[Source]" in s and "[Markdown]" in s:
            continue
        if s.startswith("[Home]") and "[Contents]" in s:
            continue

        # Drop duplicate title headings inserted by ?action=markdown.
        if s.startswith("# ") and s[2:].strip() == title:
            continue

        out.append(ln)

    # Trim leading/trailing blank lines.
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()

    return "\n".join(out).rstrip() + "\n"


def _fix_nonstandard_markdown(md: str) -> str:
    """
    The site's ?action=markdown output contains a few nonstandard constructs.
    Normalize them so Pandoc/GitHub/typical Markdown parsers render correctly.
    """
    import re

    # Some images are emitted as: ![alt][url title]
    # Convert to: ![alt](url "title")
    md = re.sub(
        r"!\[([^\]]+)\]\[(https?://[^\s\]]+)\s+([^\]]+)\]",
        r'![\1](\2 "\3")',
        md,
    )
    # Fallback: ![alt][url] -> ![alt](url)
    md = re.sub(r"!\[([^\]]+)\]\[(https?://[^\]]+)\]", r"![\1](\2)", md)
    return md


def _write_markdown(out_path: Path, title: str, url: str, body_md: str) -> None:
    # First link under the title is the original link (kept as-is for translators).
    content = f"# {title}\n\n[{title}]({url})\n\n{body_md}"
    out_path.write_text(content, encoding="utf-8")


def fetch_all(pages: list[Page], html_dir: Path, md_dir: Path) -> None:
    _ensure_dirs(html_dir, md_dir)
    for page in pages:
        raw_html = _fetch(page.url)
        (html_dir / f"{page.title}.html").write_text(raw_html, encoding="utf-8")

        raw_md = _fetch(f"{page.url}?action=markdown")
        body_md = _strip_site_chrome(raw_md, page.title)
        body_md = _fix_nonstandard_markdown(body_md)
        _write_markdown(md_dir / f"{page.title}.md", page.title, page.url, body_md)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    html_dir = repo_root / "html" / "readthesequences" / "Fragile-Purposes-Sequence"
    md_dir = repo_root / "source"
    fetch_all(PAGES, html_dir, md_dir)


if __name__ == "__main__":
    main()
