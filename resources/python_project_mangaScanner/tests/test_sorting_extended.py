from __future__ import annotations

import pytest

from manga_scanner.sorting import natural_sort_key


@pytest.mark.parametrize(
    ("names", "expected"),
    [
        (["1.png", "10.png", "2.png"], ["1.png", "2.png", "10.png"]),
        (["ch2-p10.png", "ch2-p2.png", "ch10-p1.png"], ["ch2-p2.png", "ch2-p10.png", "ch10-p1.png"]),
        (["PAGE3.PNG", "page11.png", "page2.png"], ["page2.png", "PAGE3.PNG", "page11.png"]),
        (["cover.png", "page1.png", "page2.png"], ["cover.png", "page1.png", "page2.png"]),
        (["vol1-extra9.png", "vol1-extra10.png", "vol1-extra2.png"], ["vol1-extra2.png", "vol1-extra9.png", "vol1-extra10.png"]),
        (["ページ10.png", "ページ2.png", "ページ1.png"], ["ページ1.png", "ページ2.png", "ページ10.png"]),
        (["chapter 1 page 12.png", "chapter 1 page 3.png"], ["chapter 1 page 3.png", "chapter 1 page 12.png"]),
        (["a001.png", "a010.png", "a002.png"], ["a001.png", "a002.png", "a010.png"]),
    ],
)
def test_natural_sort_key_orders_common_manga_names(names: list[str], expected: list[str]) -> None:
    assert sorted(names, key=natural_sort_key) == expected


@pytest.mark.parametrize("value", ["", "page", "001", "chapter-12-page-003"])
def test_natural_sort_key_returns_tuple_for_all_inputs(value: str) -> None:
    assert isinstance(natural_sort_key(value), tuple)


def test_natural_sort_key_keeps_equal_numeric_names_stable() -> None:
    names = ["page1.png", "page001.png", "page0001.png"]

    assert sorted(names, key=natural_sort_key) == names
