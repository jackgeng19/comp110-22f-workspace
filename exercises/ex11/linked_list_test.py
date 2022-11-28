"""Tests for linked list utils."""

import pytest
from linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730433734"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Empty head should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_non_empty() -> None:
    """Test of value_at function."""
    linked = Node(10, Node(20, Node(30, None)))
    assert value_at(linked, 0) == 10


def test_value_at_non_empty_2() -> None:
    """Test of value_at function."""
    linked = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked, 3)


def test_max_empty() -> None:
    """Test of max function."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Test of max function."""
    linked = Node(10, Node(20, Node(30, None)))
    assert max(linked) == 30


def test_linkify_empty() -> None:
    """Test of linkify function."""
    assert linkify([]) is None


def test_linkify_non_empty() -> None:
    """Test of linkify function."""
    items = [10, 20, 30]
    assert str(linkify(items)) == str(Node(10, Node(20, Node(30, None))))


def test_linkify_one_item() -> None:
    """Test of linkify function."""
    items = [10]
    assert str(linkify(items)) == str(Node(10, None))


def test_scale_empty() -> None:
    """Test of scale function."""
    assert scale(None, 2) is None


def test_scale_non_empty() -> None:
    """Test of scale function."""
    assert str(scale(linkify([1, 2, 3]), 2)) == str(Node(2, Node(4, Node(6, None))))