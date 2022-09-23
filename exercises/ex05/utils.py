"""EX05 - Utils."""

__author__ = "730433734"


from unittest import result


def only_evens(xs:list[int]) -> list[int]:
    """Generating an all even list."""
    result: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            result.append(xs[i])
        i += 1
    return result


def concat(xs_1: list[int], xs_2: list[int]) -> list[int]:
    """Returning a list that combines two lists."""
    result: list[int] = []
    i: int = 0
    while i < len(xs_1):
        result.append(xs_1[i])
        i += 1
    i = 0
    while i < len(xs_2):
        result.append(xs_2[i])
        i += 1
    return result


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Generating a list which is a subset of the given list, between the specified start index and the end index - 1. """
    result: list[int] = []
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    if len(xs) == 0 or start > end or end == 0:
        return result
    while start < end:
        result.append(xs[start])
        start += 1
    return result