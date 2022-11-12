"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730433734"


class Simpy:
    """Class of simpified Numpy."""
    values: list[float]

    def __init__(self, nums: list[float]) -> None:
        """Constructor."""
        self.values = nums

    def __repr__(self) -> str:
        """Returns a str."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < y:
            self.values.append(x)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Its purpose is to fill in the `values` attribute with range of values, like the `range` built-in function, but in terms of `float`s."""
        assert step != 0.0
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while stop < start:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Returns the sum of all items."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload of add method."""
        result: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload of power method."""
        result: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload of equal method."""
        result: list = []
        i: int = 0
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload of greater than method."""
        result: list = []
        i: int = 0
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload of subscription method."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            result: Simpy = Simpy([])
            i: int = 0
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result