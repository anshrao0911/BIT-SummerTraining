"""Create safe sample inputs for the scanner project.

The generated files are small and synthetic. They are intended for learning and
for trying the CLI before using any real manga/manhwa file.
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLES_DIR = PROJECT_ROOT / "samples"
IMAGE_FOLDER = SAMPLES_DIR / "image_folder"
CBZ_PATH = SAMPLES_DIR / "demo_cbz.zip"
PDF_PATH = SAMPLES_DIR / "demo.pdf"


def create_page(path: Path, label: str, size: tuple[int, int] = (300, 420)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, size[0] - 16, size[1] - 16), outline="black", width=3)
    draw.text((32, 40), label, fill="black")
    draw.text((32, 72), "Synthetic BIT Training sample", fill="black")
    image.save(path)


def create_image_folder() -> None:
    if IMAGE_FOLDER.exists():
        shutil.rmtree(IMAGE_FOLDER)
    create_page(IMAGE_FOLDER / "page1.png", "Folder page 1")
    create_page(IMAGE_FOLDER / "page2.png", "Folder page 2")
    create_page(IMAGE_FOLDER / "page10.png", "Folder page 10")
    (IMAGE_FOLDER / "notes.txt").write_text("The scanner should ignore this file.\n", encoding="utf-8")


def create_cbz() -> None:
    pages_dir = SAMPLES_DIR / "_generated_pages"
    if pages_dir.exists():
        shutil.rmtree(pages_dir)
    create_page(pages_dir / "page1.png", "CBZ page 1")
    create_page(pages_dir / "page2.png", "CBZ page 2")

    CBZ_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(CBZ_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(pages_dir / "page2.png", "chapter/page2.png")
        archive.write(pages_dir / "page1.png", "chapter/page1.png")
        archive.writestr("chapter/readme.txt", "The scanner should ignore this file.")

    shutil.rmtree(pages_dir)


def create_pdf() -> None:
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    document = fitz.open()
    for page_number in range(1, 4):
        page = document.new_page(width=300, height=420)
        page.draw_rect(fitz.Rect(16, 16, 284, 404), color=(0, 0, 0), width=2)
        page.insert_text((32, 48), f"PDF page {page_number}", fontsize=18)
        page.insert_text((32, 80), "Synthetic BIT Training sample", fontsize=12)
    document.save(PDF_PATH)
    document.close()


def main() -> int:
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    create_image_folder()
    create_cbz()
    create_pdf()
    print(f"Created {IMAGE_FOLDER}")
    print(f"Created {CBZ_PATH}")
    print(f"Created {PDF_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
