#!/usr/bin/python3
"Creates a square in Python."


class Square:
    "Defines a square with a private size attribute and validation."

    def __init__(self, size=0):
        """
        Constructor method for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Description:
            Initializes a Square instance with a given size.
            The size is stored in the private __size attribute.
        """
        self.__size = size

    @property
    def size(self):
        """
        Property: size
        Description: Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Args:
            value (int): The new size value to be set.

        Description:
            Sets the size of the square.
            The new size value is validated to
            ensure it is a non-negative integer.
            If the value is valid,
            it is stored in the private __size attribute.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            # Raise a TypeError if value is not an integer
            raise TypeError("size must be an integer")
        if value < 0:   # Raise a ValueError if value is less than 0
            raise ValueError("size must be >= 0")
        self.__size = value
        # If size is valid, set the private __size attribute

    def area(self):
        """
        Method: area
        Description: Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
