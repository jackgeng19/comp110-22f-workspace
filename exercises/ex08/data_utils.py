"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730433734"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(rows: list[dict[str, str]], key: str) -> list[str]:
    """Produce a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in rows:
        result.append(row[key])
    return result


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows (e.g. `list[dict[str, str]]`) into one represented as a dictionary of columns (e.g. `dict[str, list[str]]`)."""
    result: dict[str, list[str]] = {}
    for column in rows[0]:
        result[column] = column_values(rows, column)
    return result


def head(columns: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    if num > len(columns):
        num = len(columns)
    for column in columns:
        values: list[str] = []
        i: int = 0
        while i < num:
            values.append(columns[column][i])
            i += 1
        result[column] = values
    return result


def select(columns: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = columns[name]
    return result


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in dict1:
        result[column] = dict1[column]
    for column in dict2:
        if column in result:
            for item in dict2[column]:
                result[column].append(item)
        else:
            result[column] = dict2[column]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result