#!/usr/bin/python3
"Defines a square in Python."


class Square:
    """
    Class: Square
    Description: Defines a square with a private size attribute and validation.

    Attributes:
        __size (int): The size of the square (private attribute).

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
    """

    def __init__(self, size=0):
        """
        Constructor method for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Description:
            Initializes a Square instance with a given size.
            The size is validated to ensure it is a non-negative integer.
            If the size is valid, it is stored in the private __size attribute.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            # Raise a TypeError if size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:   # Raise a ValueError if size is less than 0
            raise ValueError("size must be >= 0")
        self.__size = size
        # If size is valid, set the private __size attribute

    def area(self):
        """
        Method: area
        Description: Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2   # Returns the area of the square
