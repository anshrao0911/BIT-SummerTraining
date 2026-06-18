"""OCR helpers for the student scanner."""

from __future__ import annotations

from typing import Sequence

from manga_scanner.models import PageInput


class NullOcrEngine:
    """Default OCR engine used when no real OCR engine is provided."""

    def recognize(self, page: PageInput) -> Sequence[str]:
        """Return no text. Tests inject richer fake OCR engines."""

        return []
