from __future__ import annotations

import zipfile
from pathlib import Path

import fitz
import pytest
from PIL import Image, ImageDraw


def make_image(path: Path, size: tuple[int, int] = (120, 180), label: str = "page") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), label, fill="black")
    image.save(path)
    return path


@pytest.fixture
def image_folder(tmp_path: Path) -> Path:
    folder = tmp_path / "chapter_01"
    make_image(folder / "page10.png", label="ten")
    make_image(folder / "page2.png", label="two")
    make_image(folder / "page1.png", label="one")
    return folder


@pytest.fixture
def cbz_file(tmp_path: Path) -> Path:
    image_a = make_image(tmp_path / "src" / "chapter" / "p2.png", label="two")
    image_b = make_image(tmp_path / "src" / "chapter" / "p10.png", label="ten")
    archive = tmp_path / "demo.cbz"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.write(image_b, "chapter/p10.png")
        zf.write(image_a, "chapter/p2.png")
        zf.writestr("notes.txt", "not a page")
    return archive


@pytest.fixture
def pdf_file(tmp_path: Path) -> Path:
    path = tmp_path / "demo.pdf"
    document = fitz.open()
    for label in ("one", "two"):
        page = document.new_page(width=120, height=180)
        page.insert_text((20, 40), label)
    document.save(path)
    document.close()
    return path
