from __future__ import annotations

from pathlib import Path

from manga_scanner import cli
from manga_scanner.models import MangaScan, PageScan


def test_cli_writes_markdown_output(monkeypatch, tmp_path: Path) -> None:
    output = tmp_path / "scan.md"

    def fake_scan_source(path: str) -> MangaScan:
        return MangaScan(
            title="CLI Demo",
            source_path=Path(path),
            source_type="folder",
            pages=(PageScan(1, "page1.png", 10, 20, ("hello",), ()),),
        )

    monkeypatch.setattr(cli, "scan_source", fake_scan_source)

    exit_code = cli.main(["input-folder", "--output", str(output)])

    assert exit_code == 0
    assert output.read_text(encoding="utf-8").startswith("# CLI Demo\n")
