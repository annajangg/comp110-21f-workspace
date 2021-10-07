"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730411065"


def test_only_evens_empty() -> None:
    """Tests if the numbers in the list are even."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_one() -> None:
    """Tests if the numbers in the list are even."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_two() -> None:
    """Tests if the numbers in the list are even."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_three() -> None:
    """Tests if the numbers in the list are even."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_negative() -> None:
    """Tests if the numbers in the list are even."""
    xs: list[int] = [-4, -4, -4]
    assert only_evens(xs) == [-4, -4, -4]


def test_sub_empty() -> None:
    """Tests giving subsets of a list."""
    assert sub([], 0, 1) == []


def test_sub_startgreater() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40], 8, 3) == []


def test_sub_startzero() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40], 0, 3) == [10, 20, 30]


def test_sub_zero() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40], 1, 0) == []


def test_sub_negative() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40, 50, 60], -1, 3) == [10, 20, 30]


def test_sub_greater() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40], 1, 5) == [20, 30, 40]


def test_sub_works() -> None:
    """Tests giving subsets of a list."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_concat_1empty2single() -> None:
    """Test if the two lists are combined."""
    assert concat([], [4]) == [4]


def test_concat_1empty2multiple() -> None:
    """Test if the two lists are combined."""
    assert concat([], [4, 5, 6, 7, 8, 9]) == [4, 5, 6, 7, 8, 9]


def test_concat_1single2empty() -> None:
    """Test if the two lists are combined."""
    assert concat([2], []) == [2]


def test_concat_1multiple2empty() -> None:
    """Test if the two lists are combined."""
    assert concat([0, 1, 2, 3], []) == [0, 1, 2, 3]


def test_concat_empty() -> None:
    """Test if the two lists are combined."""
    assert concat([], []) == []


def test_concat_identical() -> None:
    """Test if the two lists are combined."""
    assert concat([1], [1]) == [1, 1]


def test_concat_samelength() -> None:
    """Test if the two lists are combined."""
    assert concat([1, 2], [1, 3]) == [1, 2, 1, 3]


def test_concat_diff() -> None:
    """Test if the two lists are combined."""
    assert concat([3, 5], [4, 6, 8]) == [3, 5, 4, 8]