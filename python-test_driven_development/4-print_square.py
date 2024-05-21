#!/usr/bin/python3
"Prints a square with the character #"


def print_square(size):
    "TypeError: If size is not an integer."
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    "ValueError: If size is less than 0."
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
