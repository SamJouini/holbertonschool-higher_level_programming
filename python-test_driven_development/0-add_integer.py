#!/usr/bin/python3
"Adds two integers"


def add_integer(a, b=98):
    "TypeError: If either a or b is not an integer or float"
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
    "Returns the addition of a and b"