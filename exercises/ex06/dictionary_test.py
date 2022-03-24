"""Tests for dictionaries."""

__author__: str = "730518639"


import exercises.ex06.dictionary


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count


def test_invert() -> None:
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_invert_single_item() -> None:
    dict1: dict[str, str] = {}
    assert invert(dict1) == {"Jordan": "Red"}


def test_invert_many_items() -> None:
    dict1: dict[str, str] = {}
    assert invert(dict1) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}


def test_favorite_color() -> None:
    dict2: dict[str, str] = {}
    assert invert(dict2) == {}


def test_invert_favorite_color_single_item() -> None:
    dict2: dict[str, str] = {}
    assert invert(dict2) == {"Jordan": "Red"}


def test_invert_favorite_color_many_items() -> None:
    dict2: dict[str, str] = {}
    assert invert(dict2) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green"}


def test_invert_favorite_color_many_items_again() -> None:
    dict2: dict[str, str] = {}
    assert invert(dict2) == {"Jordan": "Red", "Neida": "Blue", "Aaron": "Green", "Julian": "Green"}


def test_count() -> None:
    list3: list = list()
    assert count(list3) == ()


def test_count_single_item() -> None:
    list3: list = list()
    assert count(list3) == ("Red") 


def test_count_many_items() -> None:
    list3: list = list()
    assert count(list3) == ("Red", "Blue", "Green")