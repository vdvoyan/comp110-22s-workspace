"""Defining functions to be tested111."""

__author__: str = "730518639"


list_int: list = list([input("Enter a list: ")])
a: int = int(input("Enter start index: "))
b: int = int(input("Enter end index: "))


def sub(list_int) -> list:
    short_list = list()
    i: int = a
    while i < b:
        short_list.append(list_int[i])
        i += 1
    return short_list


print(sub(list_int))