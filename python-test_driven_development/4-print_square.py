#!/usr/bin/python3
"Prints a square with the character #"


def print_square(size):
    """
    Prints a square of the given size using the # character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer,
        a TypeError is raised with the message "size must be an integer".
        ValueError: If size is less than 0,
        a ValueError is raised with the message "size must be >= 0".
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    "ValueError: If size is less than 0."
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
