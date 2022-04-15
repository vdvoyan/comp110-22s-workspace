"""Tests for dictionaries."""

__author__: str = "730518639"


from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Empty case."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_invert_single_item() -> None:
    """Single case."""
    dict1: dict[str, str] = {"Whatever": "Test"}
    assert invert(dict1) == {"Test": "Whatever"}


def test_invert_many_items() -> None:
    """Many cases."""
    dict1: dict[str, str] = {"Red": "Jordan", "Blue": "Neida", "Green": "Aaron"}
    assert invert(dict1) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}


def test_favorite_color() -> None:
    """Empty case."""
    dict2: dict[str, str] = {}
    assert favorite_color(dict2) == {}


def test_favorite_color_single_item() -> None:
    """Single case."""
    dict2: dict[str, str] = {"Red": "Jordan"}
    assert invert(dict2) == {"Jordan": "Red"}


def test_favorite_color_many_items() -> None:
    """Many cases."""
    dict2: dict[str, str] = {"Red": "Jordan", "Blue": "Neida", "Green": "Aaron"}
    assert invert(dict2) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}


def test_favorite_color_many_items_again() -> None:
    """Many cases again."""
    dict2: dict[str, str] = {"Red": "Jordan", "Blue": "Neida", "Green": "Aaron", "Purple": "Julian"}
    assert invert(dict2) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green", "Julian": "Purple"}


def test_count() -> None:
    """Empty case."""
    list3: list = list()
    assert count(list3) == count()


def test_count_single_item() -> None:
    """Single case."""
    list3: list = list()
    assert count(list3) == count(["Red"]) 


def test_count_many_items() -> None:
    """Many cases."""
    list3: list = list()
    assert count(list3) == count(["Red", "Blue", "Green"])