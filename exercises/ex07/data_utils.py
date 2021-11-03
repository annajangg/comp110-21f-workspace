"""Utility functions."""

__author__ = "730411065"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
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
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(given: dict[str, list[str]], how_many: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    if how_many >= len(given):
        return given
    for x, y in given.items():
        values: list[str] = []
        i: int = 0
        while i < how_many:
            values.append(y[i])
            i += 1
        result[x] = values
    return result

    # result: dict[str, list[str]] = {}
    # entry: str = ""
    # i: int = 0
    # for entry in given:
    # oldlist: list[str] = given[entry]
    # newlist: list[str] = []
    # for item in oldlist:
    # while i <= how_many:
    #     newlist.append(item)
    #     i += 1
    # result[entry] = newlist
    # return result
    
    # result: dict[str, list[str]] = {}
    # column: str = ""
    # i: int = 0
    # for column in given:
    # newlist: list[str] = []
    # for item in given[column]:
    # while i <= how_many:
    # newlist.append(item)
    # i += 1
    # result[given[column[item]]] = newlist
    # return result


def select(given: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Makes a new column-based table with specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for x, y in given.items():
        for name in names:
            if name == x:
                result[x] = y
    return result


def concat(given1: dict[str, list[str]], given2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two tables combined."""
    result: dict[str, list[str]] = {}
    for x, y in given1.items():
        result[x] = y
    for a, b in given2.items():
        if a in result.keys():
            combined: list[str] = []
            for value in result[a]:
                combined.append(value)
            for value in b:
                combined.append(value)
            result[a] = combined
        else:
            result[a] = b
    return result