"""EX07 - Dictionary."""

__author__ = "730433734"


from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test for invert function."""
    assert invert({}) == {}


def test_invert_case1() -> None:
    """Test for invert function."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_case2() -> None:
    """Test for invert function."""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_single() -> None:
    """Test for favorite_color function."""
    assert favorite_color({"Marc": "yellow"}) == "yellow"


def test_favorite_color_tie() -> None:
    """Test for favorite_color function."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue"}) == "yellow"


def test_favorite_color() -> None:
    """Test for favorite_color function."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_count_empty() -> None:
    """Test for count function."""
    assert count([]) == {}


def test_count_case1() -> None:
    """Test for count function."""
    assert count([1, 2, 3]) == {1: 1, 2: 1, 3: 1}


def test_count_case2() -> None:
    """Test for count function."""
    assert count([1, 2, 3, 1, 2, 1]) == {1: 3, 2: 2, 3: 1}