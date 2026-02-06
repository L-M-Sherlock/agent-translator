#!/usr/bin/env python3
"""
Check repo-specific Markdown formatting conventions.

Run after each translation batch. Exits non-zero on errors.

Checks:
- No Chinese italics (single *...* or _..._) outside code.
- Spacing around Markdown links based on whether the link text boundary is Chinese vs ASCII.
- The first link under the H1 in each translation file matches the original (done/) first link.
- Link/image URL destinations in each translation file match the original (done/) file.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


RE_CJK = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")
RE_ASCII_ALNUM = re.compile(r"[A-Za-z0-9]")


def is_cjk(ch: str) -> bool:
    return bool(ch) and bool(RE_CJK.search(ch))


def is_ascii_alnum(ch: str) -> bool:
    return bool(ch) and bool(RE_ASCII_ALNUM.match(ch))


def strip_code(md: str) -> str:
    # Remove fenced code blocks, then inline code, to avoid flagging code samples.
    md = re.sub(r"```.*?```", "```CODE```", md, flags=re.DOTALL)
    md = re.sub(r"`[^`]*`", "`CODE`", md)
    return md


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    kind: str
    message: str


def find_line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def extract_first_link_after_h1(md: str) -> tuple[str, str] | None:
    lines = md.splitlines()
    saw_h1 = False
    for line in lines:
        if not saw_h1:
            if line.startswith("# "):
                saw_h1 = True
            continue
        if not line.strip():
            continue
        m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)\s*$", line.strip())
        if m:
            return m.group(1), m.group(2)
        # Stop early if we hit another heading before finding a link.
        if line.lstrip().startswith("#"):
            return None
        # Otherwise keep scanning; some files have a URL-only link line etc.
    return None


def iter_links(md: str):
    # Simple link tokenizer; good enough for these notes.
    # Yields: (start_index, end_index, link_text, url)
    for m in re.finditer(r"\[([^\]]+)\]\(([^)\s]+)\)", md):
        yield m.start(), m.end(), m.group(1), m.group(2)


def _iter_inline_links_and_images(md: str):
    """
    Iterate inline markdown links and images.

    Notes:
    - Callers should pass strip_code(...) output to ignore code blocks/snippets.
    - Destinations may include an optional title: (url "title"). We only keep the URL.
    """

    # Group 1: optional '!' (image marker)
    # Group 2: link text / alt text
    # Group 3: destination (url + optional title)
    for m in re.finditer(r"(!?)\[([^\]]+)\]\(([^)\n]+)\)", md):
        dest = (m.group(3) or "").strip()
        if not dest:
            continue

        # CommonMark allows titles: (url "title"). Only compare the URL portion.
        url = dest.split()[0]
        if url.startswith("<") and url.endswith(">"):
            url = url[1:-1]

        yield (m.group(1) == "!"), (m.group(2) or ""), url


def _url_counter(md: str, *, include_images: bool) -> Counter[str]:
    c: Counter[str] = Counter()
    text = strip_code(md)
    for is_image, _text, url in _iter_inline_links_and_images(text):
        if is_image and not include_images:
            continue
        if (not is_image) and include_images:
            continue
        c[url] += 1
    return c


def check_link_urls_match_original(
    translation_path: Path, translation_raw: str, done_path: Path, done_raw: str
) -> list[Finding]:
    """
    Ensure the translation preserves all inline link/image destinations.

    We compare URL multisets (Counter), not link texts, since link texts are translated.
    """
    findings: list[Finding] = []

    done_links = _url_counter(done_raw, include_images=False)
    trans_links = _url_counter(translation_raw, include_images=False)
    done_imgs = _url_counter(done_raw, include_images=True)
    trans_imgs = _url_counter(translation_raw, include_images=True)

    missing_links = done_links - trans_links
    extra_links = trans_links - done_links
    missing_imgs = done_imgs - trans_imgs
    extra_imgs = trans_imgs - done_imgs

    if not (missing_links or extra_links or missing_imgs or extra_imgs):
        return findings

    def _fmt(counter: Counter[str]) -> str:
        items = counter.most_common(5)
        parts = [f"{n}x {u}" for u, n in items]
        suffix = "" if len(counter) <= 5 else f" (and {len(counter) - 5} more)"
        return "; ".join(parts) + suffix

    msg_parts: list[str] = []
    if missing_links:
        msg_parts.append(f"missing link URL(s): {_fmt(missing_links)}")
    if extra_links:
        msg_parts.append(f"extra link URL(s): {_fmt(extra_links)}")
    if missing_imgs:
        msg_parts.append(f"missing image URL(s): {_fmt(missing_imgs)}")
    if extra_imgs:
        msg_parts.append(f"extra image URL(s): {_fmt(extra_imgs)}")

    findings.append(
        Finding(
            path=translation_path,
            line=1,
            kind="link-urls",
            message="Link/image URL mismatch vs original (done/): "
            + "; ".join(msg_parts),
        )
    )
    return findings


def check_no_chinese_italics(path: Path, raw: str) -> list[Finding]:
    findings: list[Finding] = []
    text = strip_code(raw)

    # Single-asterisk italics containing CJK.
    for m in re.finditer(r"(?<!\*)\*([^*\n]*?)\*(?!\*)", text):
        if RE_CJK.search(m.group(1) or ""):
            findings.append(
                Finding(
                    path=path,
                    line=find_line_number(text, m.start()),
                    kind="chinese-italics",
                    message="Avoid italics for Chinese; use **bold** or quotes.",
                )
            )

    # Single-underscore italics containing CJK.
    #
    # Note: underscores are extremely common inside URLs and identifiers (e.g. `Piotr_Wozniak`).
    # To avoid false positives, only treat `_..._` as emphasis when it's surrounded by
    # whitespace or punctuation (i.e. not in the middle of a word/URL).
    for m in re.finditer(r"(?<!_)_([^_\n]+?)_(?!_)", text):
        inner = m.group(1) or ""
        if not RE_CJK.search(inner):
            continue

        before = text[m.start() - 1] if m.start() - 1 >= 0 else ""
        after = text[m.end()] if m.end() < len(text) else ""

        before_ok = before == "" or before.isspace() or before in "([{\"'“「『"
        after_ok = (
            after == "" or after.isspace() or after in ")]}\"'”」』，。！？；：、.!?;:"
        )

        if before_ok and after_ok:
            findings.append(
                Finding(
                    path=path,
                    line=find_line_number(text, m.start()),
                    kind="chinese-italics",
                    message="Avoid italics for Chinese; use **bold** or quotes.",
                )
            )

    return findings


def check_bold_spacing(path: Path, raw: str) -> list[Finding]:
    """Disallow spaces between Chinese bold spans and adjacent Chinese characters."""

    findings: list[Finding] = []
    text = strip_code(raw)

    # Match **...** that doesn't span newlines.
    for m in re.finditer(r"(?<!\*)\*\*([^*\n]*?)\*\*(?!\*)", text):
        inner = m.group(1) or ""
        if not inner:
            continue

        last = inner[-1]
        first = inner[0]

        # After bold: "**中** 文" should be "**中**文" if the bold text ends with CJK.
        end = m.end()
        if is_cjk(last) and end < len(text) and text[end] in " \t":
            k = end
            while k < len(text) and text[k] in " \t":
                k += 1
            if k < len(text) and is_cjk(text[k]):
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, end),
                        kind="bold-spacing",
                        message="Remove the space(s) after a Chinese bold span when the next character is Chinese.",
                    )
                )

        # Before bold: "中 **文**" should be "中**文**" if the bold text begins with CJK.
        start = m.start()
        if is_cjk(first) and start - 1 >= 0 and text[start - 1] in " \t":
            j = start - 1
            while j >= 0 and text[j] in " \t":
                j -= 1
            if j >= 0 and is_cjk(text[j]):
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, start),
                        kind="bold-spacing",
                        message="Remove the space(s) before a Chinese bold span when the previous character is Chinese.",
                    )
                )

    return findings


def check_link_spacing(path: Path, raw: str) -> list[Finding]:
    findings: list[Finding] = []
    text = strip_code(raw)

    for start, end, link_text, _url in iter_links(text):
        if not link_text:
            continue

        prev = text[start - 1] if start - 1 >= 0 else ""
        next_ch = text[end] if end < len(text) else ""

        first = link_text[0]
        last = link_text[-1]

        # If the link text begins with CJK, avoid inserting spaces between surrounding CJK and '['.
        # E.g. "...的[助记媒介](...)" not "...的 [助记媒介](...)".
        if first and is_cjk(first) and prev == " ":
            j = start - 2
            while j >= 0 and text[j] == " ":
                j -= 1
            if j >= 0 and is_cjk(text[j]):
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, start),
                        kind="link-spacing",
                        message="Remove the space before a Chinese-titled link when the previous character is Chinese.",
                    )
                )

        # Before '['
        if is_cjk(prev):
            if is_ascii_alnum(first):
                # Chinese + English link text should have a space: "中文 [Gary Bernhardt](...)"
                # If prev is CJK, then start-1 is that CJK; therefore, if there is no space,
                # it must be adjacent (i.e. prev isn't a space already).
                # Here, adjacency is guaranteed because prev is the immediate char.
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, start),
                        kind="link-spacing",
                        message="Add a space between Chinese and an English-titled link (before '[').",
                    )
                )
            elif is_cjk(first):
                # Chinese + Chinese link text: should be tight. If there's a space, we'd have seen prev=' '.
                pass

        # After ')'
        if is_cjk(next_ch):
            if is_ascii_alnum(last):
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, end),
                        kind="link-spacing",
                        message="Add a space between an English-titled link and following Chinese (after ')').",
                    )
                )
            elif is_cjk(last):
                # Ensure no space between ')' and CJK when link text ends in CJK.
                # If there is a space, next_ch would be ' ' not CJK, so nothing to do.
                pass

        # Special-case: avoid ')卡' with any space(s) when the link text ends with CJK.
        # E.g. "...[间隔重复记忆系统](...)卡片" not "...[间隔重复记忆系统](...) 卡片".
        if is_cjk(last) and end < len(text) and text[end] in " \t":
            k = end
            while k < len(text) and text[k] in " \t":
                k += 1
            if k < len(text) and is_cjk(text[k]):
                findings.append(
                    Finding(
                        path=path,
                        line=find_line_number(text, end),
                        kind="link-spacing",
                        message="Remove the space(s) after a Chinese-titled link when the next character is Chinese.",
                    )
                )

    return findings


def check_first_link_matches_original(
    translation_path: Path, translation_raw: str, done_path: Path, done_raw: str
) -> list[Finding]:
    findings: list[Finding] = []
    t = extract_first_link_after_h1(translation_raw)
    d = extract_first_link_after_h1(done_raw)
    if not d:
        return findings
    if not t:
        findings.append(
            Finding(
                path=translation_path,
                line=1,
                kind="first-link",
                message=f"Missing first link under H1; expected {d[0]} ({d[1]}).",
            )
        )
        return findings
    if t != d:
        findings.append(
            Finding(
                path=translation_path,
                line=2,
                kind="first-link",
                message=f"First link under H1 should match original: expected {d[0]} ({d[1]}), got {t[0]} ({t[1]}).",
            )
        )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repo root (default: .)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    translation_dir = root / "translation"
    done_dir = root / "done"

    if not translation_dir.exists():
        print("translation/ not found; nothing to check.", file=sys.stderr)
        return 0

    findings: list[Finding] = []

    for path in sorted(translation_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        findings.extend(check_no_chinese_italics(path, raw))
        findings.extend(check_bold_spacing(path, raw))
        findings.extend(check_link_spacing(path, raw))

        done_path = done_dir / path.name
        if done_path.exists():
            done_raw = done_path.read_text(encoding="utf-8")
            findings.extend(
                check_first_link_matches_original(path, raw, done_path, done_raw)
            )
            findings.extend(
                check_link_urls_match_original(path, raw, done_path, done_raw)
            )

    if findings:
        print("Formatting check failed:\n", file=sys.stderr)
        for f in findings:
            rel = f.path.relative_to(root) if f.path.is_absolute() else f.path
            print(f"- {rel}:{f.line} [{f.kind}] {f.message}", file=sys.stderr)
        print(f"\nTotal: {len(findings)} issue(s).", file=sys.stderr)
        return 1

    print("Formatting check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
