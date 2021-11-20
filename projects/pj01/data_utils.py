"""Utility functions."""

__author__ = "730411065"

from csv import DictReader


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
    for x, y in given.items():
        if how_many >= len(y):
            return given
        values: list[str] = []
        i: int = 0
        while i < how_many:
            values.append(y[i])
            i += 1
        result[x] = values
    return result


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


def count(freq: list[str]) -> dict[str, int]:
    """Function to count the frequency the numbers come up."""
    result = {}
    for item in freq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def down_indexed(given: list[str]) -> list[str]:
    """Makes a list of the indices in which the option chosen was less than 5 hours."""
    indexes = []
    i: int = 0
    while i < len(given):
        number: int = i
        if given[i] == "None" or given[i] == "0 to 2 hours" or given[i] == "3 to 5 hours":
            indexes.append(number)
        i += 1
    return indexes


def up_indexed(given: list[str]) -> list[str]:
    """Makes a list of the indices in which the option chosen was more than 5 hours."""
    indexes = []
    i: int = 0
    while i < len(given):
        number: int = i
        if given[i] == "5 to 10 hours" or given[i] == "10+ hours":
            indexes.append(number)
        i += 1
    return indexes


def specified_hours(given: list[str], index_list: list[str]) -> list[str]:
    """Uses the list of indices to get the otpions in the other list at those indices."""
    result = []
    i: int = 0
    while i < len(index_list):
        a: int = int(index_list[i])
        value: str = given[a]
        result.append(value)
        i += 1
    return result


def count_down(given: list[str]) -> int:
    """Function to count the frequency the numbers (under 5 hours) come up."""
    counter: int = 0
    for item in given:
        if item == "None" or item == "0 to 2 hours" or item == "3 to 5 hours":
            counter += 1
    return counter


def count_up(given: list[str]) -> int:
    """Function to count the frequency the numbers (above 5 hours) come up."""
    counter: int = 0
    for item in given:
        if item == "5 to 10 hours" or item == "10+ hours":
            counter += 1
    return counter
