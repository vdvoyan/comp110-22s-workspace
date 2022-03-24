"""Defining functions to be tested."""

__author__: str = "730518639"


list1: list = list(input("Enter a list: "))


def only_evens(list1) -> list:
    list2 = list()
    for x in list1:
        if x % 2 == 0:
            list2.append(x)
    return list2

print(only_evens(list1))

list1: list = list(input("Enter the first list: "))
list2: list = list(input("Enter the second list: "))
def concat(list1, list2) -> list:
    new_list = list[list1+list2]


print(concat(list1, list2))
