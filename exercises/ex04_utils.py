"""EX04 - Utils."""

__author__ = "730433734"

import re


def all(input_list: list[int], number: int) -> bool:
    """Check whether all numbers in list match the input integer."""
    is_match: bool = True
    i: int = 0
    while i < len(input_list) and is_match is True:
        if input_list[i] != number:
            is_match = False
            return is_match
        else:
            i += 1
    return is_match


def max(input_list: list[int]) -> int:
    """Return the largest number in the list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    result: int = input_list[0]
    index: int = 0
    while index < len(input_list):
        if input_list[index] >= result:
            result = input_list[index]
        else:
            index += 1
    return result


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True if lists are equal, False otherwise."""
    if len(list_1) != len(list_2):
        return False
    result: bool = True
    i: int = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            result = False
            return result
        else:
            i += 1
    return result