"""EX04 - Utils."""

__author__ = "730433734"


def all(xs: list[int], number: int) -> bool:
    """Check whether all numbers in list match the input integer."""
    if len(xs) == 0:
        return False
    is_match: bool = True
    i: int = 0
    while i < len(xs):
        if xs[i] != number:
            is_match = False
            return is_match
        else:
            i += 1
    return is_match


def max(input: list[int]) -> int:
    """Return the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    elif len(input) == 1:
        return input[0]
    elif len(input) > 1:
        result: int = input[0]
        next_index: int = 1
        while next_index < len(input):
            if input[next_index] >= result:
                result = input[next_index]
            next_index += 1
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