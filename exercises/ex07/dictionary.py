"""EX07 - Dictionary."""

__author__ = "730433734"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Return a dict[str, str] that inverts the keys and the values of parameter dict."""
    result: dict[str, str] = {}
    for key in xs:
        for item in result:
            if xs[key] == item:
                raise KeyError
        result[xs[key]] = key
    return result


def favorite_color(xs: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    result: dict[str, int] = {}
    for key in xs:
        if xs[key] in result:
            result[xs[key]] += 1
        else:
            result[xs[key]] = 1
    n: int = 0
    favorite: str = ""
    for item in result:
        if result[item] > n:
            favorite = item
            n = result[item]
    return favorite


def count(xs: list[str]) -> dict[str, int]:
    """Produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for x in xs:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result