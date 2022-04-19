"""Testing the functions defined."""

__author__: str = "730518639"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Empty case."""
    input_list: list[int] = list()
    assert only_evens(input_list) == only_evens(list())


def test_only_evens_usage_one() -> None:
    """First use case."""
    input_list: list[int] = list([1, 2, 3, 4, 5])
    assert only_evens(input_list) == only_evens(list([2, 4]))


def test_only_evens_usage_two() -> None:
    """Second use case."""
    input_list: list[int] = list([8, 17, 6, 41, 9])
    assert only_evens(input_list) == only_evens(list([8, 6]))


def test_sub() -> None:
    """Empty case."""
    a_list: list[int] = list([])
    int_1: int = int()
    int_2: int = int()
    assert sub(a_list, int_1, int_2) == sub(list([]), int_1, int_2)


def test_sub_usage_one() -> None:
    """First use case."""
    a_list: list[int] = list([8, 61, 16, 58])
    int_1: int = int(1)
    int_2: int = int(3)
    assert sub(a_list, int_1, int_2) == sub(list([61, 16]), int_1, int_2)


def test_sub_usage_two() -> None:
    """Second use case."""
    a_list: list[int] = list([9, 17, 51, 68, 37, 84])
    int_1: int = int(2)
    int_2: int = int(6)
    assert sub(a_list, int_1, int_2) == sub(list([51, 68, 37, 84]), int_1, int_2)


def test_sub_usage_three() -> None:
    """Third use case."""
    a_list: list[int] = list([9, 45, 37, 89])
    int_1: int = int(-3)
    int_2: int = int(2)
    assert sub(a_list, int_1, int_2) == sub(list([9, 45]), int_1, int_2)


def test_sub_usage_four() -> None:
    """Fourth use case."""
    a_list: list[int] = list([4, 11, 81, 95])
    int_1: int = int(0)
    int_2: int = int(3)
    assert sub(a_list, int_1, int_2) == sub(list([4, 11, 81]), int_1, int_2)


def test_concat() -> None:
    """Empty case."""
    list_1: list[int] = list()
    list_2: list[int] = list()
    assert concat(list_1, list_2) == concat(list(), list())


def test_concat_usage_one() -> None:
    """First use case."""
    list_1: list[int] = list([1, 2, 3])
    list_2: list[int] = list([4, 5, 6])
    assert concat(list_1, list_2) == concat(list([1, 2, 3]), list([4, 5, 6]))


def test_concat_usage_two() -> None:
    """Second use case."""
    list_1: list[int] = list([1, 60, 27])
    list_2: list[int] = list([4, 91, 43])
    assert concat(list_1, list_2) == concat(list([1, 60, 27]), list([4, 91, 43]))