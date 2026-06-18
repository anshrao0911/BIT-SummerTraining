# Project Walkthrough

This project is a small scanner pipeline.

```text
input path
   |
   v
load_pages(path)
   |
   v
PageInput objects
   |
   v
scan_source(path, ocr_engine)
   |
   v
MangaScan result
   |
   v
render_markdown(scan)
   |
   v
Markdown text
   |
   v
manga-scan CLI writes .md file
```

## Main Files

### `sorting.py`

This file solves page ordering.

Normal string sorting is wrong for manga pages:

```text
page1.png
page10.png
page2.png
```

Natural sorting should produce:

```text
page1.png
page2.png
page10.png
```

### `loaders.py`

This file turns input files into `PageInput` objects.

It must support:

- folders of images
- one image file
- `.cbz` and `.zip` archives
- PDFs

It must also reject:

- missing files
- unsupported extensions
- empty folders or archives
- corrupt images, archives, or PDFs

### `scanner.py`

This file connects page loading with OCR.

The tests use fake OCR engines so your project does not need Tesseract or a paid AI API.

The scanner must:

- call OCR once per page
- strip blank OCR text
- warn when no text is detected
- warn when a page is very tall like a manhwa page
- return a `MangaScan`

### `markdown.py`

This file turns a `MangaScan` into final Markdown text.

It must:

- include source metadata
- include one section per page
- include page dimensions
- include OCR text
- include warnings
- escape Markdown-sensitive characters

## Important Models

### `PageInput`

Represents one loaded image page before OCR.

### `PageScan`

Represents one page after OCR and warning detection.

### `MangaScan`

Represents the full result for one scanned source.

## How To Think

Do not memorize the answer. Follow the data.

Ask:

1. What input does this function receive?
2. What exact output should it return?
3. What errors should it raise?
4. Which test proves that behavior?
5. What is the smallest correct implementation?
