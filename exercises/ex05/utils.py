"""List utility functions part 2."""

__author__ = "730411065"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that were even."""
    only_even_list: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            only_even_list.append(xs[i])
        i += 1
    return only_even_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a list which is a subset of the given list between the specificed start and end index."""
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    sub_list: list[int] = []
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return sub_list
    else:
        while start < end:
            sub_list.append(a_list[start])
            start += 1
        return sub_list


def concat(first_list: list[int], sec_list: list[int]) -> list[int]:
    """Returns a list that contains all the elements of the first list followed by all of the elements of the second list."""
    comb_list: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(first_list):
        comb_list.append(first_list[i])
        i += 1
    while j < len(sec_list):
        comb_list.append(sec_list[j])
        j += 1
    return comb_list