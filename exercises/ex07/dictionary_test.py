"""Tests the dictionary functions using two use cases and one edge case."""

__author__ = "730562389"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_use1() -> None:
    """Tests the invert function to check if it correctly inverts the key-value pairs of a given dictionary with a use case."""
    # Use cases
    my_dict: dict[str, str] = {
        "a": "z",
        "b": "y",
        "c": "x"
    }
    assert invert(my_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Tests the invert function to check if it correctly inverts the key-value pairs of a given dictionary with a use case."""
    my_dict1: dict[str, str] = {
        "chocolate": "vanilla",
        "strawberry": "shortcake",
        "eggs": "toast",
    }
    assert invert(my_dict1) == {'vanilla': 'chocolate', 'shortcake': 'strawberry', 'toast': 'eggs'}


def test_invert_edge() -> None:
    """Tests the invert function to check if it correctly inverts the key-value pairs of a given dictionary with an edge case."""
    # Edge case
    my_dict2: dict[str, str] = {}
    assert invert(my_dict2) == {}
    with pytest.raises(KeyError):
        my_dict4 = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dict4)


def test_favorite_color1() -> None:
    """Tests the favorite_color function to check if it returns the favorite color from the input in a dictionary with a use case."""
    # Use cases
    my_dict: dict[str, str] = {
        "Ishaan": "Blue",
        "Messi": "Yellow",
        "Cristiano": "Red",
        "Ronaldo": "Red"
    }
    assert favorite_color(my_dict) == "Red"


def test_favorite_color2() -> None:
    """Tests the favorite_color function to check if it returns the favorite color from the input in a dictionary with a use case."""
    my_dict1: dict[str, str] = {
        "Ishaan": "Blue",
        "Smaran": "Blue",
        "Sanat": "Red",
        "Varun": "Blue",
        "Ani": "Green",
        "Prateek": "Yellow"
    }
    assert favorite_color(my_dict1) == "Blue"


def test_favorite_color3() -> None:
    """Tests the favorite_color function to check if it returns the favorite color from the input in a dictionary with an edge case."""
    # Edge case 
    my_dict2: dict[str, str] = {
        "Ishaan": "Blue",
        "Drithi": "Green"
    }
    assert favorite_color(my_dict2) == "Blue"


def test_count1() -> None:
    """Tests the count function to see if it counts the number of the occurrences of a string in a list with a use case."""
    # Use case
    my_list: list[str] = ["When", "Why", "When", "Why", "When"]
    assert count(my_list) == {'When': 3, 'Why': 2}


def test_count2() -> None:
    """Tests the count function to see if it counts the number of the occurrences of a string in a list with a use case."""
    my_list1: list[str] = ["Ishaan", "Balakrishnan", "Drithi", "Ishaan", "Balakrishnan", "Ishaan", "Drithi"]
    assert count(my_list1) == {'Ishaan': 3, 'Balakrishnan': 2, 'Drithi': 2}


def test_count3() -> None:
    """Tests the count function to see if it counts the number of the occurrences of a string in a list with an edge case."""
    # Edge case
    my_list2: list[str] = []
    assert count(my_list2) == {}