#!/usr/bin/python3
"Creates a square in Python."


class Square:
    "Defines a square with a private size attribute and validation."

    def __init__(self, size=0):
        "Initializes a Square instance with a given size."
        self.__size = size

    @property
    def size(self):
        "Retrieves the size of the square."
        return self.__size

    @size.setter
    def size(self, value):
        "Sets the size of the square."
        if not isinstance(value, int):
            "If `value` is not an integer."
            raise TypeError("size must be an integer")
        if value < 0:
            "If `value` is less than 0."
            raise ValueError("size must be >= 0")
        self.__size = value
        "If size is valid, set the private __size attribute"

    def area(self):
        "Calculates the area of the square."
        return self.__size ** 2
        "Returns: The area of the square."
