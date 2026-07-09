from __future__ import annotations

from pathlib import Path

import pytest

from manga_scanner import cli
from manga_scanner.models import MangaScan, PageScan


def fake_scan(path: str) -> MangaScan:
    return MangaScan(
        title="CLI",
        source_path=Path(path),
        source_type="folder",
        pages=(PageScan(1, "page1.png", 10, 20, ("text",), tuple()),),
    )


def test_cli_prints_to_stdout_when_output_is_omitted(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "scan_source", fake_scan)

    exit_code = cli.main(["input-folder"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith("# CLI\n")


def test_cli_supports_short_output_flag(monkeypatch, tmp_path: Path) -> None:
    output = tmp_path / "out.md"
    monkeypatch.setattr(cli, "scan_source", fake_scan)

    exit_code = cli.main(["input-folder", "-o", str(output)])

    assert exit_code == 0
    assert output.read_text(encoding="utf-8").startswith("# CLI\n")


def test_cli_creates_utf8_output_file(monkeypatch, tmp_path: Path) -> None:
    output = tmp_path / "unicode.md"

    def scan_with_unicode(path: str) -> MangaScan:
        return MangaScan(
            title="魔法",
            source_path=Path(path),
            source_type="folder",
            pages=(PageScan(1, "ページ1.png", 10, 20, ("こんにちは",), tuple()),),
        )

    monkeypatch.setattr(cli, "scan_source", scan_with_unicode)

    cli.main(["input-folder", "--output", str(output)])

    assert "こんにちは" in output.read_text(encoding="utf-8")


def test_build_parser_requires_input() -> None:
    parser = cli.build_parser()

    with pytest.raises(SystemExit):
        parser.parse_args([])
