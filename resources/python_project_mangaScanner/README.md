# Manga/Manhwa Markdown Scanner

This is a Python assignment scaffold. Students complete the TODO-marked functions so the scanner can read manga/manhwa sources and produce a Markdown report.

Start here:

```text
START_HERE.md
```

Then read:

- `PROJECT_WALKTHROUGH.md`
- `TRY_SAMPLE_INPUTS.md`
- `PROGRESS_CHECKLIST.md`

## What The Scanner Supports

- Image folders containing `.png`, `.jpg`, `.jpeg`, or `.webp` pages
- `.cbz` and `.zip` comic archives
- PDF files rendered into page images
- Pluggable OCR through a simple `OcrEngine` interface
- Markdown output with source metadata, page dimensions, OCR text, and warnings

## Student Setup

Python 3.9 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

Run one focused test file:

```bash
pytest tests/test_markdown.py -v
```

Run the CLI after implementing the TODOs:

```bash
python scripts/create_demo_cbz.py
manga-scan samples/demo_cbz.zip --output scan.md
```

## Student Task

Complete the TODOs in:

- `src/manga_scanner/sorting.py`
- `src/manga_scanner/loaders.py`
- `src/manga_scanner/scanner.py`
- `src/manga_scanner/markdown.py`

Do not change the tests just to make them pass. Use the tests as a specification.

Before submitting, fill in `IMPLEMENTATION_NOTES.md`. Your teacher may ask you to explain your code.

## Optional Real PDF Test

Most tests generate small images/PDFs automatically. If your teacher gives you a local manga PDF path, run:

```bash
REAL_MANGA_PDF="/path/to/manga.pdf" pytest
```
