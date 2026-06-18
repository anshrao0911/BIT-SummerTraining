from manga_scanner.sorting import natural_sort_key


def test_natural_sort_orders_embedded_numbers_numerically() -> None:
    names = ["page10.png", "page2.png", "page1.png", "page11.png"]

    assert sorted(names, key=natural_sort_key) == [
        "page1.png",
        "page2.png",
        "page10.png",
        "page11.png",
    ]


def test_natural_sort_is_case_insensitive_for_text_parts() -> None:
    names = ["Page2.PNG", "page10.png", "page1.png"]

    assert sorted(names, key=natural_sort_key) == [
        "page1.png",
        "Page2.PNG",
        "page10.png",
    ]
