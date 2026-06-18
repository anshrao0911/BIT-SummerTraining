# Start Here: Manga/Manhwa Markdown Scanner

Welcome to your Week 1 BIT Training Python project.

You are building a command-line scanner that can read manga/manhwa pages from:

- an image folder
- one image file
- a `.cbz` or `.zip` archive
- a PDF

The scanner turns those pages into a Markdown report.

## 1. Setup

Run these commands inside this project folder:

```bash
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest --collect-only -q
```

Windows PowerShell activation:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
pytest --collect-only -q
```

You should see the tests collected. The full test suite will fail at first because the TODO functions are not complete.

## 2. Understand Your Mission

Only four files contain the main TODO work:

```text
src/manga_scanner/sorting.py
src/manga_scanner/loaders.py
src/manga_scanner/scanner.py
src/manga_scanner/markdown.py
```

Do not start with all tests. Work in this order.

## 3. Solve In Stages

### Stage 1: Sorting

```bash
pytest tests/test_sorting.py tests/test_sorting_extended.py -v
```

Goal: make page names sort correctly, so `page2.png` comes before `page10.png`.

### Stage 2: Loading Pages

```bash
pytest tests/test_loaders.py tests/test_loaders_extended.py tests/test_edge_cases.py -v
```

Goal: load folders, single images, CBZ/ZIP archives, and PDFs.

### Stage 3: Scanning

```bash
pytest tests/test_scanner.py tests/test_scanner_extended.py -v
```

Goal: connect loaded pages to the OCR engine and warnings.

### Stage 4: Markdown

```bash
pytest tests/test_markdown.py tests/test_markdown_extended.py -v
```

Goal: produce a clean, exact Markdown report.

### Stage 5: CLI

```bash
pytest tests/test_cli.py tests/test_cli_extended.py -v
```

Goal: make the `manga-scan` command write reports.

## 4. Try Real Sample Inputs

Generate safe sample files:

```bash
python scripts/create_sample_inputs.py
```

After you complete enough TODOs, try:

```bash
manga-scan samples/image_folder --output folder_scan.md
manga-scan samples/demo_cbz.zip --output cbz_scan.md
manga-scan samples/demo.pdf --output pdf_scan.md
```

Open the `.md` files and check the output.

## 5. Final Submission

Before submitting, run:

```bash
pytest
```

Then submit:

- your completed code
- terminal screenshot or copied output showing tests passed
- generated `folder_scan.md`, `cbz_scan.md`, or `pdf_scan.md`
- completed `IMPLEMENTATION_NOTES.md`

Your teacher may ask you to explain your logic.
