"""EX04 - List Utility Functions - Practice with lists in functions."""


__author__ = "730562389"


def all(int1_list: list[int], int1: int) -> bool:
    """Function all determines if each number is int 1 list is equal to the integer in int 1."""
    counter: int = 0
    same_value: bool = True
    if len(int1_list) == 0:
        return False 
    while counter < len(int1_list):
        if int1_list[counter] != int1:
            return False
        counter += 1
    return same_value


def max(int1_list: list[int]) -> int:
    """Funcation max determines the max integer value within the given list."""
    if len(int1_list) == 0:
        raise ValueError("max() arg is an empty list")
    max_val: int = int1_list[0]
    counter: int = 0
    while counter < len(int1_list): 
        if max_val < int1_list[counter]:
            max_val = int1_list[counter]
        counter += 1
    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function is_equal is made to determine if two different lists are equal to eachother."""
    counter: int = 0
    if len(list1) != len(list2):
        return False
    while counter < len(list1):
        if list1[counter] != list2[counter]:
            return False
        counter += 1
    return True