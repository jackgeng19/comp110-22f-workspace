"""EX05 - Utils_test."""

__author__ = "730433734"


from tkinter import N
from utils import only_evens, concat, sub


def test_only_even_empty() -> None:
    xs: list[float] = []
    assert only_evens(xs) == []


def test_only_even_odd() -> None:
    xs: list[float] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_even_many() -> None:
    xs: list[float] = [1, 5, 3, 4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_concat_empty() -> None:
    xs_1: list[int] = []
    xs_2: list[int] = []
    assert concat(xs_1, xs_2) == []


def test_concat_many() -> None:
    xs_1: list[int] = [1, 3, 5]
    xs_2: list[int] = [2, 4 ,6]
    assert concat(xs_1, xs_2) == [1, 3, 5, 2, 4, 6]


def test_concat_single() -> None:
    xs_1: list[int] = [5]
    xs_2: list[int] = [19]
    assert concat(xs_1, xs_2) == [5, 19]


def test_sub_empty() -> None:
    xs: list[int] = []
    assert sub(xs, 0, 1) == []


def test_sub_great_start() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 4, 3) == []


def test_sub_zero_end() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 2, 0) == []


def test_sub_neg_start() -> None:
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, -1, 3) == [1, 2, 3]


def test_sub_great_end() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 2, 5) == [6, 8]


def test_sub_normal() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert sub(xs, 1, 3) == [4, 6]