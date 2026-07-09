from __future__ import annotations

import zipfile
from pathlib import Path

import pytest
from PIL import Image

from manga_scanner.errors import CorruptSourceError, EmptySourceError, SourceNotFoundError, UnsupportedSourceError
from manga_scanner.loaders import load_pages


def make_image(path: Path, size: tuple[int, int] = (64, 96), mode: str = "RGB") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new(mode, size, 255 if mode == "L" else "white")
    image.save(path)
    return path


@pytest.mark.parametrize("extension", [".png", ".jpg", ".jpeg", ".webp", ".PNG", ".JPG"])
def test_load_pages_accepts_supported_image_extensions(tmp_path: Path, extension: str) -> None:
    page = make_image(tmp_path / f"page1{extension}")

    pages = load_pages(page)

    assert len(pages) == 1
    assert pages[0].source_name == page.name
    assert pages[0].image.mode == "RGB"


def test_load_pages_converts_grayscale_images_to_rgb(tmp_path: Path) -> None:
    page = make_image(tmp_path / "gray.png", mode="L")

    pages = load_pages(page)

    assert pages[0].image.mode == "RGB"


def test_load_pages_ignores_subdirectories_inside_folder(tmp_path: Path) -> None:
    folder = tmp_path / "chapter"
    make_image(folder / "page2.png")
    make_image(folder / "page1.png")
    make_image(folder / "nested" / "page0.png")

    pages = load_pages(folder)

    assert [page.source_name for page in pages] == ["page1.png", "page2.png"]


def test_load_pages_rejects_corrupt_image_file(tmp_path: Path) -> None:
    image = tmp_path / "bad.png"
    image.write_bytes(b"not an image")

    with pytest.raises(CorruptSourceError):
        load_pages(image)


@pytest.mark.parametrize("extension", [".cbz", ".zip", ".CBZ", ".ZIP"])
def test_load_pages_accepts_archive_extensions_case_insensitively(tmp_path: Path, extension: str) -> None:
    image = make_image(tmp_path / "page1.png")
    archive = tmp_path / f"book{extension}"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.write(image, "page1.png")

    pages = load_pages(archive)

    assert [page.source_name for page in pages] == ["page1.png"]


def test_load_pages_ignores_archive_directory_entries(tmp_path: Path) -> None:
    image = make_image(tmp_path / "page1.png")
    archive = tmp_path / "book.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("chapter/", "")
        zf.write(image, "chapter/page1.png")

    pages = load_pages(archive)

    assert [page.source_name for page in pages] == ["chapter/page1.png"]


def test_load_pages_rejects_corrupt_image_inside_archive(tmp_path: Path) -> None:
    archive = tmp_path / "book.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("page1.png", b"not an image")

    with pytest.raises(CorruptSourceError):
        load_pages(archive)


def test_load_pages_raises_precise_missing_path_error(tmp_path: Path) -> None:
    missing = tmp_path / "missing.cbz"

    with pytest.raises(SourceNotFoundError, match="missing.cbz"):
        load_pages(missing)


@pytest.mark.parametrize("filename", ["book.rar", "book.7z", "notes.md", "image.gif"])
def test_load_pages_rejects_unsupported_file_extensions(tmp_path: Path, filename: str) -> None:
    file_path = tmp_path / filename
    file_path.write_bytes(b"data")

    with pytest.raises(UnsupportedSourceError):
        load_pages(file_path)


def test_load_pages_pdf_page_numbers_are_one_based(pdf_file: Path) -> None:
    pages = load_pages(pdf_file)

    assert [page.page_number for page in pages] == [1, 2]


def test_load_pages_preserves_each_page_image_object(image_folder: Path) -> None:
    pages = load_pages(image_folder)

    assert len({id(page.image) for page in pages}) == len(pages)


def test_load_pages_empty_archive_error_mentions_archive_path(tmp_path: Path) -> None:
    archive = tmp_path / "empty.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("notes.txt", "ignore")

    with pytest.raises(EmptySourceError, match="empty.cbz"):
        load_pages(archive)
