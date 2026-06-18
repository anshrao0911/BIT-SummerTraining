# Try Sample Inputs

Tests are important, but you should also see the scanner output.

First generate safe sample files:

```bash
python scripts/create_sample_inputs.py
```

This creates:

```text
samples/image_folder/page1.png
samples/image_folder/page2.png
samples/image_folder/page10.png
samples/demo_cbz.zip
samples/demo.pdf
```

## After Stage 2: Check Loading

You can inspect whether pages load in Python:

```bash
python -c "from manga_scanner.loaders import load_pages; print([p.source_name for p in load_pages('samples/image_folder')])"
```

Expected shape:

```text
['page1.png', 'page2.png', 'page10.png']
```

## After Stage 3: Check Scanner

```bash
python -c "from manga_scanner.scanner import scan_source; scan = scan_source('samples/image_folder'); print(scan.title, scan.source_type, len(scan.pages))"
```

Expected shape:

```text
image_folder folder 3
```

## After Stage 4 and 5: Use CLI

```bash
manga-scan samples/image_folder --output folder_scan.md
manga-scan samples/demo_cbz.zip --output cbz_scan.md
manga-scan samples/demo.pdf --output pdf_scan.md
```

Open `folder_scan.md`. The report should look like:

```markdown
# image\_folder

- Source: `samples/image_folder`
- Type: folder
- Pages: 3

## Page 1

- Source page: `page1.png`
- Dimensions: 300 x 420
```

The default OCR engine returns no text, so warnings like this are normal:

```markdown
### Warnings

- No OCR text detected\.
```

## Optional Real PDF

If your teacher gives you a local PDF path:

```bash
manga-scan "/path/to/manga.pdf" --output real_scan.md
```

Do not commit or upload copyrighted PDFs.
