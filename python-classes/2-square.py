#!/usr/bin/python3
"Defines a square in Python."


class Square:
    "Defines a square with a private size attribute and validation."
    def __init__(self, size=0):
        "Initializes a Square instance with a given size."
        if not isinstance(size, int):
            "Check if size is an integer"
            raise TypeError("size must be an integer")
            "If `size` is not an integer."
        if size < 0:
            "If `size` is less than 0."
            raise ValueError("size must be >= 0")
        self.__size = size
        "If size is valid, set the private __size attribute"
