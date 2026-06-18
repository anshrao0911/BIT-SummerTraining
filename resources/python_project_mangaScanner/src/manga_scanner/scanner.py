"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.models import MangaScan, OcrEngine


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    """Scan a source and return OCR-ready Markdown data.

    Expected behavior:
    - Use ``load_pages`` to read the source.
    - Use ``NullOcrEngine`` when ``ocr_engine`` is ``None``.
    - Strip empty OCR blocks.
    - Add a warning when a page has no OCR text.
    - Add a warning for very tall manhwa-style pages.

    TODO: Implement scan orchestration.
    """

    raise NotImplementedError("TODO: implement scan_source")
