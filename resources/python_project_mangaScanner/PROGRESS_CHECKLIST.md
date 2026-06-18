# Progress Checklist

Tick each item as you complete it.

## Setup

- [ ] Python 3.9 or newer works
- [ ] Virtual environment is activated
- [ ] `python -m pip install -e ".[dev]"` completed
- [ ] `pytest --collect-only -q` shows tests

## Stage 1: Sorting

- [ ] `pytest tests/test_sorting.py -v` passes
- [ ] `pytest tests/test_sorting_extended.py -v` passes
- [ ] I can explain natural sorting

## Stage 2: Loading

- [ ] Single image loading works
- [ ] Folder loading works
- [ ] CBZ/ZIP loading works
- [ ] PDF loading works
- [ ] Empty/corrupt/unsupported inputs raise correct errors
- [ ] Loader tests pass

## Stage 3: Scanning

- [ ] OCR engine is called once per page
- [ ] Blank OCR text is removed
- [ ] Blank page warning works
- [ ] Long vertical page warning works
- [ ] Scanner tests pass

## Stage 4: Markdown

- [ ] Markdown title and metadata work
- [ ] Page sections work
- [ ] OCR text list works
- [ ] Warning section works
- [ ] Markdown escaping works
- [ ] Markdown tests pass

## Stage 5: CLI

- [ ] `manga-scan samples/image_folder --output folder_scan.md` works
- [ ] `manga-scan samples/demo_cbz.zip --output cbz_scan.md` works
- [ ] `manga-scan samples/demo.pdf --output pdf_scan.md` works
- [ ] CLI tests pass

## Final

- [ ] `pytest` passes
- [ ] I filled `IMPLEMENTATION_NOTES.md`
- [ ] I can explain every TODO I completed
