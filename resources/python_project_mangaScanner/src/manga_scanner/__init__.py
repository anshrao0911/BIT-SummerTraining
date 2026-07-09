"""Student-facing API for the manga/manhwa Markdown scanner assignment."""

from manga_scanner.loaders import load_pages
from manga_scanner.markdown import render_markdown
from manga_scanner.models import MangaScan, OcrEngine, PageInput, PageScan
from manga_scanner.scanner import scan_source
from manga_scanner.sorting import natural_sort_key

__all__ = [
    "MangaScan",
    "OcrEngine",
    "PageInput",
    "PageScan",
    "load_pages",
    "natural_sort_key",
    "render_markdown",
    "scan_source",
]
