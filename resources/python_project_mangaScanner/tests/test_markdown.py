from pathlib import Path

from manga_scanner.markdown import render_markdown
from manga_scanner.models import MangaScan, PageScan


def test_render_markdown_outputs_exact_report() -> None:
    scan = MangaScan(
        title="Demo *Chapter*",
        source_path=Path("/books/demo.cbz"),
        source_type="archive",
        pages=(
            PageScan(
                page_number=1,
                source_name="page1.png",
                width=120,
                height=180,
                text_blocks=("Hello *hero*", "What next?"),
                warnings=(),
            ),
            PageScan(
                page_number=2,
                source_name="page2.png",
                width=120,
                height=180,
                text_blocks=(),
                warnings=("No OCR text detected.",),
            ),
        ),
    )

    assert render_markdown(scan) == """# Demo \\*Chapter\\*

- Source: `/books/demo.cbz`
- Type: archive
- Pages: 2

## Page 1

- Source page: `page1.png`
- Dimensions: 120 x 180

### OCR Text

1. Hello \\*hero\\*
2. What next?

## Page 2

- Source page: `page2.png`
- Dimensions: 120 x 180

### OCR Text

_No text detected._

### Warnings

- No OCR text detected\\.
"""
