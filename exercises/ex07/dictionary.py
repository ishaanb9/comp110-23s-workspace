"""EX07 - Dictionaries - Different functions that use dictionaries for different outputs!!!"""


__author__ = "730562389"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values in the dictinary by swapping them with eachother."""
    keyval: str = ""
    dict_1: dict[str, str] = {}
    for key in my_dict:
        keyval = my_dict[key]
        if keyval in dict_1:
            raise KeyError("Multiple of the same key value")
        dict_1[keyval] = key
    return dict_1


def favorite_color(colors: dict[str, str]) -> str:
    """Function that finds the most common favorite color from different peoples favorite colors."""
    keyval: str = ""
    color_no: dict[str, int] = {}
    for key in colors:
        keyval = colors[key]
        if keyval in color_no:
            color_no[keyval] += 1
        else:
            color_no[keyval] = 1
    key_maximum: str = ""
    number_maximum: int = 0
    for key in color_no:
        if color_no[key] > number_maximum:
            number_maximum = color_no[key]
            key_maximum = key
    return key_maximum
        

def count(my_dict: list[str]) -> dict[str, int]:
    """Function that records the number of occurances of each value in a given list."""
    dict_2: dict[str, int] = {}
    for keyval in my_dict:
        if keyval in dict_2:
            dict_2[keyval] += 1
        else:
            dict_2[keyval] = 1
    return dict_2