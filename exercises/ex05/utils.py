"""Defining functions to be tested."""

__author__: str = "730518639"


def only_evens(input_list: list[int]) -> list[int]:
    """Given a list of integers, returns a list composed of only even integers."""
    empty_list: list[int] = list()
    for i in input_list:
        if i % 2 == 0:
            empty_list.append(i)
    return empty_list


def sub(a_list: list[int], int_1: int, int_2: int) -> list[int]:
    """Given a list of ints, starting int and ending int, returns list from start to end, not inclusive."""
    b_list: list[int] = list()
    for i in a_list:
        if len(a_list) == 0:
            return b_list
        else:
            while a_list.index in range(int_1, int_2 - 1):
                b_list.append(a_list[i])
    return b_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combines two given lists of integers into one."""
    list_3: list[int] = list()
    for i in list_1:
        while list_1.index in range(len(list_1)):
            list_3.append(list_1[i])
    for i in list_2:    
        while list_2.index in range(len(list_2)):
            list_3.append(list_2[i])
    return list_3