"""Markdown rendering for scanner results."""

from __future__ import annotations

from manga_scanner.models import MangaScan


def render_markdown(scan):
    def esc(text: str) -> str:
        return text.replace("[", "\\[").replace("]", "\\]")

    lines = []

    lines.append(f"# {esc(scan.title)}")
    lines.append("")
    lines.append(f"- Source: {scan.source_path}")
    lines.append(f"- Type: {scan.source_type}")
    lines.append("")

    for page in scan.pages:
        lines.append(f"## Page {page.page_number}")
        lines.append(f"- File: {page.source_name}")
        lines.append(f"- Size: {page.width}x{page.height}")

        if page.text_blocks:
            lines.append("- Text:")
            for t in page.text_blocks:
                lines.append(f"  - {esc(t)}")

        if page.warnings:
            lines.append("- Warnings:")
            for w in page.warnings:
                lines.append(f"  - {esc(w)}")

        lines.append("")

    return "\n".join(lines)
