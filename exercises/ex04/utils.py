"""List utility functions."""

__author__ = "730411065"


# TODO: Implement your functions here.
def all(xs: list[int], x: int) -> bool:
    """Find if all ints in the list the same as given int."""
    i: int = 0
    if len(xs) == 0:
        return False
    while i < len(xs):
        if xs[i] != x:
            return False
        i += 1
    return True


def is_equal(first: list[int], second: list[int]) -> bool:
    """Find if every element at every index is equal in both lists."""
    i: int = 0
    if len(first) != len(second):
        return False
    while i < len(first):
        if first[i] != second[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Find the biggest int in the list."""
    i: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = input[0]
    while i < len(input):
        if input[i] > max_num:
            max_num = input[i]
        i += 1
    return max_num