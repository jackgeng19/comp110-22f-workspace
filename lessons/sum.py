"""Example of Sum Function."""

def sum(xs: list) -> float:
    a: float = 0.0
    i: int = 0
    while i < len(xs):
        a += xs[i]
        i += 1
    return a