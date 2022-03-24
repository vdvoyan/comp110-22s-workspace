"""Dictionary Functions."""


__author__: str = "730518639"


n = int(input("Enter the number of elements in dictionary: "))

dict1 = {}
# Asks for number of key-values and adds to empty dictionary defined above.
for i in range(n):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dict1.update({key: value})


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionary."""
    inv_dict: dict = {}
    for key in dict1:
        val = dict1[key]
        inv_dict[val] = key
    print(inv_dict)
    return(inv_dict)


invert(dict1)


n1 = int(input("Enter the number of elements in dictionary: "))

dict2 = {}
# Asks for number of key-values and adds to empty dictionary defined above.
for i in range(n1):
    key = input("Enter a name: ")
    value = input("Enter a color: ")
    dict2.update({key: value})


def favorite_color(dict2: dict[str, str]):
    """Returns the mode color or the first one if there is a tie."""
    mode_dict: dict = {}
    for key, value in dict2.items():
        if value not in mode_dict:
            mode_dict[value] = 0
        else:
            mode_dict[value] += 1
        if mode_dict[value] != 0:
            print(max(mode_dict))
        else:
            list2: list = list(dict2.values())
    print(list2[0])
    return(mode_dict)


favorite_color(dict2)

list3 = list(input("Enter the number of elements in list: "))


def count(list3: list = list()):
    empty_dict: dict = {}
    for item in list3:
        if (item in empty_dict):
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1

    for key, value in empty_dict.items():
        print(key, value)


count(list3)