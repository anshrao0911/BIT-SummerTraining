from __future__ import annotations

from pathlib import Path

from PIL import Image

from manga_scanner.models import PageInput
from manga_scanner.scanner import scan_source


class RecordingOcr:
    def __init__(self) -> None:
        self.calls: list[tuple[int, str]] = []

    def recognize(self, page: PageInput) -> list[str]:
        self.calls.append((page.page_number, page.source_name))
        return [f" text for {page.source_name} ", "", "   "]


def make_image(path: Path, size: tuple[int, int] = (100, 120)) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, "white").save(path)
    return path


def test_scan_source_calls_ocr_once_per_page_in_order(image_folder: Path) -> None:
    ocr = RecordingOcr()

    scan = scan_source(image_folder, ocr_engine=ocr)

    assert ocr.calls == [(1, "page1.png"), (2, "page2.png"), (3, "page10.png")]
    assert [page.text_blocks for page in scan.pages] == [
        ("text for page1.png",),
        ("text for page2.png",),
        ("text for page10.png",),
    ]


def test_scan_source_default_ocr_marks_each_page_blank(image_folder: Path) -> None:
    scan = scan_source(image_folder)

    assert all(page.text_blocks == tuple() for page in scan.pages)
    assert all(page.warnings == ("No OCR text detected.",) for page in scan.pages)


def test_scan_source_sets_title_and_type_for_single_image(tmp_path: Path) -> None:
    image = make_image(tmp_path / "cover.page1.png")

    scan = scan_source(image, ocr_engine=RecordingOcr())

    assert scan.title == "cover.page1"
    assert scan.source_type == "image"
    assert len(scan.pages) == 1


def test_scan_source_sets_type_for_cbz(cbz_file: Path) -> None:
    scan = scan_source(cbz_file, ocr_engine=RecordingOcr())

    assert scan.source_type == "archive"
    assert scan.title == "demo"


def test_scan_source_sets_type_for_pdf(pdf_file: Path) -> None:
    scan = scan_source(pdf_file, ocr_engine=RecordingOcr())

    assert scan.source_type == "pdf"
    assert scan.title == "demo"


def test_scan_source_does_not_warn_for_non_vertical_page(tmp_path: Path) -> None:
    folder = tmp_path / "normal"
    make_image(folder / "page1.png", size=(200, 499))

    scan = scan_source(folder, ocr_engine=RecordingOcr())

    assert "Long vertical manhwa-style page." not in scan.pages[0].warnings


def test_scan_source_warns_at_vertical_threshold(tmp_path: Path) -> None:
    folder = tmp_path / "vertical"
    make_image(folder / "page1.png", size=(200, 500))

    scan = scan_source(folder, ocr_engine=RecordingOcr())

    assert "Long vertical manhwa-style page." in scan.pages[0].warnings


class TupleOcr:
    def recognize(self, page: PageInput) -> tuple[str, ...]:
        return ("first", " second ")


def test_scan_source_accepts_sequence_from_ocr_engine(image_folder: Path) -> None:
    scan = scan_source(image_folder, ocr_engine=TupleOcr())

    assert scan.pages[0].text_blocks == ("first", "second")
