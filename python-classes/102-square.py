#!/usr/bin/python3
"Creates a square in Python."


class Square:
    "Defines a square with a private size attribute and validation."

    def __init__(self, size=0):
        "Initializes a Square instance with a given size."
        self.__size = size

    @property   # Getter for the size attribute
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

    def __eq__(self, other):
        "Compares the area of the square with another square."
        return self.area() == other.area()
        "Returns: True if the areas are equal, False otherwise."

    def __ne__(self, other):
        "Compares the area of the square with another square."
        return self.area() != other.area()
        "Returns: True if the areas are not equal, False otherwise."

    def __gt__(self, other):
        "Compares the area of the square with another square."
        return self.area() > other.area()
        """Returns: True if the area is > than the other square's area,
        False otherwise."""

    def __ge__(self, other):
        "Compares the area of the square with another square."
        return self.area() >= other.area()
        """Returns: True if the area is > than or = to the other square's area,
        False otherwise."""

    def __lt__(self, other):
        "Compares the area of the square with another square."
        return self.area() < other.area()
        """Returns:
        True if the area is < than the other square's area,
        False otherwise."""

    def __le__(self, other):
        "Compares the area of the square with another square."
        return self.area() <= other.area()
        """Returns:
        True if the area is < than or = to the other square's area,
        False otherwise."""
