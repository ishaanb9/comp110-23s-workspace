"""EX05 - Using utility functions!"""


__author__ = "730562389"


def only_evens(ints: list[int]) -> list[int]:
    """Takes a list and returns the even numbers in it."""
    counter: int = 0
    num_even: list[int] = list()
    while counter < len(ints):
        if (ints[counter] % 2) == 0:
            num_even.append(ints[counter])
        counter += 1
    return num_even  


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Takes two lists and combines them."""
    combined: list[int] = list()
    counter: int = 0
    while counter < len(list1):
        combined.append(list1[counter])
        counter += 1
    counter = 0
    while counter < len(list2):
        combined.append(list2[counter])
        counter += 1
    return combined


def sub(range: list[int], num_start: int, num_end: int) -> list[int]:
    """Returns a range of integers from a different list."""
    list_new: list[int] = list()
    if len(range) == 0 or (num_start > num_end) or (num_end <= 0):
        return list_new
    if num_start < 0:
        num_start = 0
    if num_end > len(range):
        num_end = len(range)
    while num_start < num_end:
        list_new.append(range[num_start])
        num_start += 1
    return list_new