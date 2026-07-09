"""Markdown rendering for scanner results."""

from __future__ import annotations

from manga_scanner.models import MangaScan


def render_markdown(scan: MangaScan) -> str:
    """Render a deterministic Markdown report.

    Expected format:
    - ``# <title>``
    - Source metadata bullets
    - One ``## Page N`` section per page
    - Dimensions, OCR text, and warnings
    - Escape Markdown-sensitive text where needed

    TODO: Implement Markdown rendering.
    """

    raise NotImplementedError("TODO: implement render_markdown")
