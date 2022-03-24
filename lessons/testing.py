"""Defining functions to be tested."""

__author__: str = "730518639"


list_int: list = list([input("Enter a list: ")])
a: int = int(input("Enter start index: "))
b: int = int(input("Enter end index: "))


def sub(list_int) -> list:
    if a in range(len(list_int)) and b in range(len(list_int)) and a < b:
        short_list = list([])
        i: int = a
        while i < b:
            short_list.append(list_int[i])
            i += 1
        return short_list
    else:
        print("That's not in range!")
        exit()


sub(list_int)