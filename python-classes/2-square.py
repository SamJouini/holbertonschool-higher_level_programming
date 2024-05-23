#!/usr/bin/python3
"Defines a square in Python."


class Square:
    """
    Class: Square
    Description: Defines a square with a private size attribute and validation.
    """

    def __init__(self, size=0):
        # initializes a Square instance with a given size.
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
        if not isinstance(size, int):   # Check if size is an integer
            raise TypeError("size must be an integer")
        # If `size` is not an integer.
        if size < 0:   # `size` is less than 0.
            raise ValueError("size must be >= 0")
        self.__size = size
        # If size is valid, set the private __size attribute
