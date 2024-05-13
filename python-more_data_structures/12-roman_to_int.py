#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not (isinstance(roman_string, str) and roman_string):
        return 0

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_num[char]
        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result
