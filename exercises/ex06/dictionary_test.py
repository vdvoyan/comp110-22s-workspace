"""Tests for dictionaries."""

__author__: str = "730518639"


from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Empty case."""
    dict_1: dict[str, str] = {}
    assert invert(dict_1) == {}


def test_invert_single_item() -> None:
    """Single case."""
    dict_1: dict[str, str] = {"Whatever": "Test"}
    assert invert(dict_1) == {"Test": "Whatever"}


def test_invert_many_items() -> None:
    """Many cases."""
    dict_1: dict[str, str] = {"Red": "Jordan", "Blue": "Neida", "Green": "Aaron"}
    assert invert(dict_1) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}


def test_favorite_color_usage_one() -> None:
    """First usage case."""
    dict_2: dict[str, str] = {"Jordan": "Red", "Neida": "Blue", "Aaron": "Red"}
    assert favorite_color(dict_2) == favorite_color("Red")


def test_favorite_color_usage_two() -> None:
    """Second usage case."""
    dict_2: dict[str, str] = {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}
    assert favorite_color(dict_2) == favorite_color("Red")


def test_favorite_color_usage_three() -> None:
    """Third usage case."""
    dict_2: dict[str, str] = {"Jordan": "Blue", "Neida": "Blue", "Aaron": "Green", "Julian": "Purple"}
    assert favorite_color(dict_2) == favorite_color("Blue")


def test_count() -> None:
    """Empty case."""
    list_3: list = list()
    assert count(list_3) == count()


def test_count_single_item() -> None:
    """Single case."""
    list_3: list = list()
    assert count(list_3) == count(["Red"]) 


def test_count_many_items() -> None:
    """Many cases."""
    list_3: list = list()
    assert count(list_3) == count(["Red", "Blue", "Green"])