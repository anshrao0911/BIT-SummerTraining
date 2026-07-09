from pathlib import Path

import pytest

from manga_scanner.errors import EmptySourceError, SourceNotFoundError, UnsupportedSourceError
from manga_scanner.loaders import load_pages


def test_load_pages_reads_image_folder_in_natural_order(image_folder: Path) -> None:
    pages = load_pages(image_folder)

    assert [page.page_number for page in pages] == [1, 2, 3]
    assert [page.source_name for page in pages] == [
        "page1.png",
        "page2.png",
        "page10.png",
    ]
    assert [(page.width, page.height) for page in pages] == [(120, 180)] * 3


def test_load_pages_reads_cbz_without_extracting(cbz_file: Path) -> None:
    pages = load_pages(cbz_file)

    assert [page.source_name for page in pages] == ["chapter/p2.png", "chapter/p10.png"]
    assert all(page.width == 120 and page.height == 180 for page in pages)


def test_load_pages_reads_pdf_pages(pdf_file: Path) -> None:
    pages = load_pages(pdf_file)

    assert [page.page_number for page in pages] == [1, 2]
    assert [page.source_name for page in pages] == ["page-1", "page-2"]
    assert all(page.width > 0 and page.height > 0 for page in pages)


def test_load_pages_rejects_missing_source(tmp_path: Path) -> None:
    with pytest.raises(SourceNotFoundError):
        load_pages(tmp_path / "missing")


def test_load_pages_rejects_unsupported_file(tmp_path: Path) -> None:
    unsupported = tmp_path / "notes.txt"
    unsupported.write_text("not manga", encoding="utf-8")

    with pytest.raises(UnsupportedSourceError):
        load_pages(unsupported)


def test_load_pages_rejects_empty_folder(tmp_path: Path) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()

    with pytest.raises(EmptySourceError):
        load_pages(empty)
