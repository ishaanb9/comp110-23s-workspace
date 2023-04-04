"""EX05 test - Test using utility functions!"""


__author__ = "730562389"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests the function when given an empty input for the list."""
    ints: list[int] = []
    assert only_evens(ints) == []


def test_evens_for_only_evens() -> None:
    """Tests the function when given a list with even numbers."""
    ints: list[int] = [2, 4, 6, 8, 10, 12, 26, 38]
    assert only_evens(ints) == [2, 4, 6, 8, 10, 12, 26, 38]


def test_odds_for_only_evens() -> None:
    """Tests the function when given a list with odd numbers."""
    ints: list[int] = [1, 27, 97, 723, 937]
    assert only_evens(ints) == []


def test_concat_empty() -> None:
    """Tests the function when given an empty input."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_numbers() -> None:
    """Tests if the function concat works as intended and combines both the integers from both lists."""
    list1: list[int] = [2, 4, 6, 8, 10, 12, 26, 38]
    list2: list[int] = [1, 27, 97, 723, 937]
    assert concat(list1, list2) == [2, 4, 6, 8, 10, 12, 26, 38, 1, 27, 97, 723, 937]


def test_concat_with_one_list_empty() -> None:
    """Tests if it the function works when one list is empty."""
    list1: list[int] = []
    list2: list[int] = [55, 98, 47, 948]
    assert concat(list1, list2) == [55, 98, 47, 948]


def test_sub_out_of_range() -> None:
    """Tests if the function works when the start and end integers are out of range."""
    range: list[int] = [17, 47, 48, 94, 26]
    num_start: int = -10
    num_end: int = 7
    assert sub(range, num_start, num_end) == [17, 47, 48, 94, 26]


def test_sub_with_empty_list() -> None:
    """Gives the sub function an empty lists and checks to see if it returns an empty list."""
    range: list[int] = []
    num_start: int = 2
    num_end: int = 4
    assert sub(range, num_start, num_end) == []


def test_sub_numbers_with_start_and_end() -> None:
    """Tests to see if the sub function returns the correct integers from the start to end index."""
    range: list[int] = [1, 3, 5, 7, 9]
    num_start: int = 2
    num_end: int = 4
    assert sub(range, num_start, num_end) == [5, 7]