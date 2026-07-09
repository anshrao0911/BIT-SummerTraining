"""Create a tiny demo CBZ fixture for local CLI practice."""

from __future__ import annotations

import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "samples" / "demo_cbz.zip"


def make_page(path: Path, label: str) -> None:
    image = Image.new("RGB", (300, 420), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((20, 20, 280, 400), outline="black", width=3)
    draw.text((40, 60), label, fill="black")
    image.save(path)


def main() -> int:
    temp_dir = PROJECT_ROOT / "samples" / "_demo_pages"
    temp_dir.mkdir(parents=True, exist_ok=True)
    page_one = temp_dir / "page1.png"
    page_two = temp_dir / "page2.png"
    make_page(page_one, "Demo page 1")
    make_page(page_two, "Demo page 2")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(page_one, "page1.png")
        archive.write(page_two, "page2.png")

    print(f"Created {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
