"""Command-line entry point for manga-scan."""

from __future__ import annotations

import argparse
from pathlib import Path

from manga_scanner.markdown import render_markdown
from manga_scanner.scanner import scan_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan manga/manhwa into Markdown.")
    parser.add_argument("input", help="Image folder, CBZ/ZIP archive, or PDF file")
    parser.add_argument(
        "--output",
        "-o",
        help="Markdown output path. Prints to stdout when omitted.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    markdown = render_markdown(scan_source(args.input))
    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
