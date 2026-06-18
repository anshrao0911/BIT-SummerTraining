"""Load manga/manhwa pages from folders, CBZ/ZIP archives, and PDFs."""

from pathlib import Path
from PIL import Image
import zipfile
from pdf2image import convert_from_path

from .models import PageInput
from .errors import (
    SourceNotFoundError,
    UnsupportedSourceError,
    EmptySourceError,
    CorruptSourceError,
)
from .sorting import natural_key


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
ARCHIVE_EXTS = {".cbz", ".zip"}
PDF_EXTS = {".pdf"}


def _load_image(path: Path):
    try:
        img = Image.open(path)
        return img.convert("RGB")
    except Exception:
        raise CorruptSourceError(str(path))


def load_pages(path: str | Path) -> list[PageInput]:
    path = Path(path)

    # ❌ Missing
    if not path.exists():
        raise SourceNotFoundError(str(path))

    pages = []

    # 📁 Folder
    if path.is_dir():
        files = [
            p for p in path.iterdir()
            if p.is_file() and p.suffix.lower() in IMAGE_EXTS
        ]

        if not files:
            raise EmptySourceError(str(path))

        files = sorted(files, key=lambda x: natural_key(x.name))

        for i, file in enumerate(files, start=1):
            img = _load_image(file)
            pages.append(PageInput(i, file.name, img))

        return pages

    # 🖼 Single Image
    if path.suffix.lower() in IMAGE_EXTS:
        img = _load_image(path)
        return [PageInput(1, path.name, img)]

    # 📦 Archive
    if path.suffix.lower() in ARCHIVE_EXTS:
        try:
            with zipfile.ZipFile(path) as zf:
                names = [
                    n for n in zf.namelist()
                    if not n.endswith("/") and Path(n).suffix.lower() in IMAGE_EXTS
                ]

                if not names:
                    raise EmptySourceError(str(path))

                names = sorted(names, key=natural_key)

                for i, name in enumerate(names, start=1):
                    try:
                        with zf.open(name) as f:
                            img = Image.open(f)
                            img = img.convert("RGB")
                            pages.append(PageInput(i, Path(name).name, img))
                    except Exception:
                        raise CorruptSourceError(str(path))

        except zipfile.BadZipFile:
            raise CorruptSourceError(str(path))

        return pages

    # 📄 PDF
    if path.suffix.lower() in PDF_EXTS:
        try:
            images = convert_from_path(path)

            if not images:
                raise EmptySourceError(str(path))

            for i, img in enumerate(images, start=1):
                pages.append(PageInput(i, f"page_{i}.png", img.convert("RGB")))

            return pages

        except Exception:
            raise CorruptSourceError(str(path))

    # ❌ Unsupported
    raise UnsupportedSourceError(str(path))
