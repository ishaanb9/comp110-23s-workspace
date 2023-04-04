"""CQ04 - Dictionary function writing"""


__author__ = "730562389"


def zip(key_string: list[str], key_value: list[int]) -> dict[str,int]:

    dictionary_key: dict[str,int] = {}

    if len(key_string) != len(key_value):
        return dictionary_key
    else:
        i: int = 0
        while i < len(key_string):
            dictionary_key[key_string[i]] = key_value[i]
            i += 1
        return dictionary_key
    
    
print (zip (["hi", "hey", "cookie"], [1, 2, 3]))

 