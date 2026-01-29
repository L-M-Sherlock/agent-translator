#!/usr/bin/env python3
"""
Pair source segments with translations and export to csv/.

Expected workflow:
1) A source CSV exists (e.g. machine_tranz/<name>.md.csv) with rows like:
   key,source[,translation]
   (Optional header row: Key,Source,...; optional comment lines starting with '#')
2) A translation file exists with one translated segment per non-empty line.
3) Export a CSV with columns: Key,Source,Translation (no Context column).

Run:
  uv run python scripts/export_csv.py --src ./machine_tranz/foo.md.csv --trans ./ai_trans/foo.md
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _read_nonempty_lines(path: Path) -> list[str]:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "":
            continue
        lines.append(line.rstrip("\n\r"))
    return lines


def _read_source_csv(path: Path) -> list[tuple[str, str]]:
    """
    Read (key, source) pairs from a CSV.
    Skips comment lines starting with '#', and skips a header row if present.
    """

    pairs: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[0].startswith("#"):
                continue
            # Trim cells.
            row = [cell.strip() for cell in row]
            if all(cell == "" for cell in row):
                continue
            if len(row) >= 2 and row[0].lower() == "key" and row[1].lower() == "source":
                continue

            if len(row) == 1:
                # Fallback: source-only input; generate a stable key later.
                pairs.append(("", row[0]))
            else:
                pairs.append((row[0], row[1]))
    return pairs


def _default_out_path(src: Path, out_dir: Path) -> Path:
    name = src.name
    if name.endswith(".md.csv"):
        name = name[: -len(".md.csv")] + ".csv"
    else:
        name = src.stem + ".csv"
    return out_dir / name


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        required=True,
        type=Path,
        help="Source CSV (e.g. ./machine_tranz/foo.md.csv)",
    )
    parser.add_argument(
        "--trans",
        required=True,
        type=Path,
        help="Translation file (one segment per non-empty line)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output CSV path (default: csv/<src>.csv)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("csv"),
        help="Output directory (default: ./csv)",
    )
    args = parser.parse_args()

    src_path: Path = args.src
    trans_path: Path = args.trans
    out_dir: Path = args.out_dir
    out_path: Path = args.out if args.out else _default_out_path(src_path, out_dir)

    src_pairs = _read_source_csv(src_path)
    trans_lines = _read_nonempty_lines(trans_path)

    if len(src_pairs) != len(trans_lines):
        raise SystemExit(
            f"Line count mismatch: source={len(src_pairs)} rows vs translation={len(trans_lines)} lines "
            f"({src_path} vs {trans_path})."
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Key", "Source", "Translation"])
        writer.writeheader()
        for i, ((key, source), translation) in enumerate(
            zip(src_pairs, trans_lines), start=1
        ):
            if not key:
                key = f"line_{i:06d}"
            writer.writerow({"Key": key, "Source": source, "Translation": translation})

    print(f"Wrote {len(trans_lines)} rows to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
