"""Dictionary Functions."""


from genericpath import exists


__author__: str = "730518639"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionary."""
    inv_dict: dict = {}
    for key in dict_1:
        val = dict_1[key]
        inv_dict[val] = key
    return(inv_dict)


def favorite_color(dict_2: dict[str, str]) -> str:
    """Returns the mode color or the first one if there is a tie."""
    mode_color: str = str()
    for value in dict_2:
        if exists(max(value)) is True:
            max(value) == mode_color
        else:
            if exists(max(value)) is False:
                value[0] == mode_color
    return(mode_color)


def count(list_3: list[str] = list()) -> dict[str, int]:
    """Counts number of items."""
    empty_dict: dict = {}
    for key, value in empty_dict.items():
        for item in list_3:
            if (item in empty_dict):
                empty_dict[item] += 1
            else:
                empty_dict[item] = 1
    return(empty_dict)