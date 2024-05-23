#!/usr/bin/python3
"Creates a square in Python."


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
            The size is validated and stored in the private __size attribute.
        """
        self.size = size

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method: area
        Description: Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method: my_print
        Description: Prints the square using the '#' character.

        If the size is 0, it prints an empty line.
        If the size is not 0, it prints a square of '#' characters
        with a length and width equal to the size.
        """
        if self.__size == 0:
            print()  # Print an empty line if size is 0
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  # Print a line of '#' characters
