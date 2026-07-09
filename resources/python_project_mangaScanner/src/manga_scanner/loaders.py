"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.models import PageInput

SUPPORTED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SUPPORTED_ARCHIVE_EXTENSIONS = {".cbz", ".zip"}


def load_pages(path: str | Path) -> list[PageInput]:
    """Load pages from an image folder, CBZ/ZIP archive, or PDF.

    Expected behavior:
    - Raise ``SourceNotFoundError`` when the path does not exist.
    - Raise ``UnsupportedSourceError`` for unsupported paths.
    - Raise ``EmptySourceError`` when no readable pages are found.
    - Return pages sorted by natural page order.

    TODO: Implement folder, archive, and PDF loading.
    """

    raise NotImplementedError("TODO: implement load_pages")
