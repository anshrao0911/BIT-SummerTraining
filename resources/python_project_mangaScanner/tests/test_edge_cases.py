from __future__ import annotations

import os
import zipfile
from pathlib import Path

import pytest
from PIL import Image

from manga_scanner.errors import CorruptSourceError, EmptySourceError
from manga_scanner.loaders import load_pages
from manga_scanner.markdown import render_markdown
from manga_scanner.models import MangaScan, PageScan
from manga_scanner.scanner import scan_source


def make_image(path: Path, size: tuple[int, int] = (120, 180)) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, "white").save(path)
    return path


def test_load_pages_ignores_non_image_files_in_folder(tmp_path: Path) -> None:
    folder = tmp_path / "mixed"
    make_image(folder / "page2.png")
    make_image(folder / "page1.png")
    (folder / "notes.txt").write_text("ignore me", encoding="utf-8")

    pages = load_pages(folder)

    assert [page.source_name for page in pages] == ["page1.png", "page2.png"]


def test_load_pages_handles_unicode_page_names(tmp_path: Path) -> None:
    folder = tmp_path / "第01話"
    make_image(folder / "ページ10.png")
    make_image(folder / "ページ2.png")

    pages = load_pages(folder)

    assert [page.source_name for page in pages] == ["ページ2.png", "ページ10.png"]


def test_load_pages_orders_nested_archive_by_page_filename(tmp_path: Path) -> None:
    first = make_image(tmp_path / "src" / "001.png")
    tenth = make_image(tmp_path / "src" / "010.png")
    archive = tmp_path / "nested.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.write(tenth, "chapter/extras/010.png")
        zf.write(first, "chapter/main/001.png")
        zf.writestr("chapter/readme.md", "ignore")

    pages = load_pages(archive)

    assert [page.source_name for page in pages] == [
        "chapter/main/001.png",
        "chapter/extras/010.png",
    ]


def test_load_pages_rejects_archive_with_no_images(tmp_path: Path) -> None:
    archive = tmp_path / "empty.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("notes.txt", "not a page")

    with pytest.raises(EmptySourceError):
        load_pages(archive)


def test_load_pages_rejects_corrupt_archive(tmp_path: Path) -> None:
    archive = tmp_path / "broken.cbz"
    archive.write_bytes(b"not a zip file")

    with pytest.raises(CorruptSourceError):
        load_pages(archive)


def test_load_pages_rejects_malformed_pdf(tmp_path: Path) -> None:
    pdf = tmp_path / "broken.pdf"
    pdf.write_bytes(b"not a real pdf")

    with pytest.raises(CorruptSourceError):
        load_pages(pdf)


def test_render_markdown_escapes_markdown_sensitive_text() -> None:
    scan = MangaScan(
        title="A [title]",
        source_path=Path("demo.cbz"),
        source_type="archive",
        pages=(
            PageScan(
                page_number=1,
                source_name="p1.png",
                width=10,
                height=20,
                text_blocks=("panel #1",),
                warnings=("check [bubble]",),
            ),
        ),
    )

    markdown = render_markdown(scan)

    assert "# A \\[title\\]" in markdown
    assert "1. panel \\#1" in markdown
    assert "- check \\[bubble\\]" in markdown


def test_real_manga_pdf_loads_when_env_var_is_set() -> None:
    pdf_path = os.environ.get("REAL_MANGA_PDF")
    if not pdf_path:
        pytest.skip("Set REAL_MANGA_PDF to run this optional real-PDF test.")

    scan = scan_source(pdf_path)

    assert scan.source_type == "pdf"
    assert len(scan.pages) >= 1
    assert scan.pages[0].width > 0
    assert scan.pages[0].height > 0
