"""Dictionary related utility functions."""

__author__ = "730518639"


from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv into a list of rows."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a column based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}

    for row in column_table:
        empty_list: list[str] = []
        number = 0
        while number < n:
            empty_list.append(column_table[row][number])
            number += 1
            if n > len(column_table[row]):
                return column_table
        result[row] = empty_list
    
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in columns:
        result[i] = column_table[i]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column based table by combining two column based tables."""
    result: dict[str, list[str]] = {}
    
    for row in first:
        result[row] = first[row]
    
    for row in second:
        if row in result:
            number = 0
            for i in second[row]:
                result[row].append(second[row][number])
                number += 1
        else:
            result[row] = second[row]

    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Counts frequencies of specific values."""
    result: dict[str, int] = {}

    for i in given_list:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    
    return result