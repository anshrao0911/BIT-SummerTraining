from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

from manga_scanner.models import PageInput
from manga_scanner.scanner import scan_source


def make_image(path: Path, size: tuple[int, int] = (120, 180), label: str = "page") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), label, fill="black")
    image.save(path)
    return path


class FakeOcr:
    def recognize(self, page: PageInput) -> list[str]:
        if page.page_number == 1:
            return ["  Hello hero!  ", "", "Next panel"]
        return ["   "]


def test_scan_source_injects_ocr_and_records_blank_page_warning(image_folder: Path) -> None:
    scan = scan_source(image_folder, ocr_engine=FakeOcr())

    assert scan.title == "chapter_01"
    assert scan.source_type == "folder"
    assert [page.text_blocks for page in scan.pages] == [
        ("Hello hero!", "Next panel"),
        tuple(),
        tuple(),
    ]
    assert "No OCR text detected." in scan.pages[1].warnings


def test_scan_source_warns_for_long_vertical_manhwa_page(tmp_path: Path) -> None:
    folder = tmp_path / "vertical"
    make_image(folder / "page1.png", size=(200, 900), label="long")

    scan = scan_source(folder, ocr_engine=FakeOcr())

    assert "Long vertical manhwa-style page." in scan.pages[0].warnings
