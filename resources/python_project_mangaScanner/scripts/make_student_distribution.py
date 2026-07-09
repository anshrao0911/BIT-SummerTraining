"""Create a student-ready zip that excludes teacher-only materials."""

from __future__ import annotations

import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "dist" / "manga_scanner_student.zip"
EXCLUDED_PARTS = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    "teacher_private",
    "dist",
    ".venv",
    ".venv312",
    "build",
    "samples/_demo_pages",
}
EXCLUDED_FILES = {
    "docs/teacher_guide.md",
}


def should_include(path: Path) -> bool:
    relative = path.relative_to(PROJECT_ROOT)
    relative_text = relative.as_posix()
    if relative_text in EXCLUDED_FILES:
        return False
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return False
    if any(relative_text.startswith(prefix + "/") for prefix in EXCLUDED_PARTS):
        return False
    return not any(part.endswith(".egg-info") for part in relative.parts)


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(PROJECT_ROOT.rglob("*")):
            if path.is_file() and should_include(path):
                archive.write(path, path.relative_to(PROJECT_ROOT))
    print(f"Created {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
