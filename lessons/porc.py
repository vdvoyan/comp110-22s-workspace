list9 = list(input("Enter the number of elements in list: "))


def count(list9: list = list()):
    empty_dict: dict = {}
    for item in list9:
        if (item in empty_dict):
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1

    for key, value in empty_dict.items():
        print(key, value)


count(list9)
exit()



value = input("Enter a value: ")
dict9.update({key: value})




list3: list[str] = list(input("Enter a list: "))


def count23(list3) -> dict[str, int]:
    """Takes list input and forms dictionary."""
    num: int = 0
    dict3 = {input(list3), num}

    for key in list3:
        if key not in list3:
            list3[num] = 0
        else:
            list3[num] += 1
    key = input(list3)
    value = num
    dict3.update({key: value})
    return(dict3)


count23(list3)

first_row: dict[str, list[str]] = column_table
    for column in first_row:
        int_N: list = list()
        for i in first_row:
            int_N.append(first_row[column])
        
        result[column].append(first_row, int_N)

    return result