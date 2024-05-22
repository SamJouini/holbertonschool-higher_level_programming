#!/usr/bin/python3
"""
A base class for geometry-related classes.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    It inherits from the Rectangle class and validates the size
    during instantiation.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
