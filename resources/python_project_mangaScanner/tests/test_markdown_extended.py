from __future__ import annotations

from pathlib import Path

import pytest

from manga_scanner.markdown import render_markdown
from manga_scanner.models import MangaScan, PageScan


def make_scan(text_blocks: tuple[str, ...] = ("hello",), warnings: tuple[str, ...] = tuple()) -> MangaScan:
    return MangaScan(
        title="Title",
        source_path=Path("source.cbz"),
        source_type="archive",
        pages=(PageScan(1, "page1.png", 10, 20, text_blocks, warnings),),
    )


@pytest.mark.parametrize(
    ("raw", "escaped"),
    [
        ("a*b", "a\\*b"),
        ("a_b", "a\\_b"),
        ("a[b]", "a\\[b\\]"),
        ("a#b", "a\\#b"),
        ("a-b", "a\\-b"),
        ("a.b", "a\\.b"),
        ("a`b`", "a\\`b\\`"),
        ("a\\b", "a\\\\b"),
    ],
)
def test_render_markdown_escapes_special_characters_in_text(raw: str, escaped: str) -> None:
    markdown = render_markdown(make_scan(text_blocks=(raw,)))

    assert f"1. {escaped}" in markdown


def test_render_markdown_contains_one_page_heading_per_page() -> None:
    scan = MangaScan(
        title="Many",
        source_path=Path("many.cbz"),
        source_type="archive",
        pages=(
            PageScan(1, "p1.png", 10, 20, ("one",), tuple()),
            PageScan(2, "p2.png", 10, 20, ("two",), tuple()),
            PageScan(3, "p3.png", 10, 20, tuple(), ("No OCR text detected.",)),
        ),
    )

    markdown = render_markdown(scan)

    assert markdown.count("## Page ") == 3
    assert "- Pages: 3" in markdown


def test_render_markdown_omits_warning_section_when_no_warnings() -> None:
    markdown = render_markdown(make_scan(warnings=tuple()))

    assert "### Warnings" not in markdown


def test_render_markdown_lists_multiple_warnings_in_order() -> None:
    markdown = render_markdown(make_scan(warnings=("first warning", "second warning")))

    assert markdown.index("- first warning") < markdown.index("- second warning")


def test_render_markdown_ends_with_single_newline() -> None:
    markdown = render_markdown(make_scan())

    assert markdown.endswith("\n")
    assert not markdown.endswith("\n\n")


def test_render_markdown_handles_scan_with_zero_pages() -> None:
    scan = MangaScan("Empty", Path("empty.cbz"), "archive", tuple())

    markdown = render_markdown(scan)

    assert "- Pages: 0" in markdown
    assert "## Page " not in markdown
