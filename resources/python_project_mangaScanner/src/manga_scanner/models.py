"""Data models for scan inputs and results."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, Sequence

from PIL import Image


@dataclass(frozen=True)
class PageInput:
    """A loaded page image ready for scanning."""

    page_number: int
    source_name: str
    image: Image.Image
    width: int
    height: int


@dataclass(frozen=True)
class PageScan:
    """OCR and diagnostic result for one scanned page."""

    page_number: int
    source_name: str
    width: int
    height: int
    text_blocks: tuple[str, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class MangaScan:
    """Complete scan result for one manga/manhwa source."""

    title: str
    source_path: Path
    source_type: str
    pages: tuple[PageScan, ...] = field(default_factory=tuple)


class OcrEngine(Protocol):
    """Minimal OCR interface used by the scanner.

    Tests can inject a fake implementation, so no system OCR binary or cloud API
    is required for this assignment.
    """

    def recognize(self, page: PageInput) -> Sequence[str]:
        """Return OCR text blocks for the given page."""
