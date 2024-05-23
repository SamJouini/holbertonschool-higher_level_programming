#!/usr/bin/python3
"Adds two integers"


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum as an integer.

    Args:
        a (int or float): The first argument to be added.
        b (int or float, optional): The second argument to be added.
        Defaults to 98 if not provided.

    Raises:
        TypeError: If either a or b is not an integer or float,
        a TypeError is raised with the message
        "a must be an integer" or "b must be an integer", respectively.

    Returns:
        int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
