"""Test fot the funtion."""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single() -> None:
    xs = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    xs = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_again() -> None:
    xs = [-1.0, 1.0, -2.0, 2.0]
    assert sum(xs) == 0.0