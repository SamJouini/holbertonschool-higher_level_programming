#!/usr/bin/python3
"Creates a square in Python."


class Square:
    """
    Class: Square
    Description: Defines a square with a private size attribute and validation.

    Attributes:
        __size (int): The size of the square (private attribute).
        __position (tuple): The position of the square (private attribute).

    Raises:
        TypeError:
            - If the provided size is not an integer.
            - If the provided position is not a tuple of 2 positive integers.
        ValueError: If the provided size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor method for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Description:
            Initializes a Square instance with a given size and position.
            The size and position are validated
            and stored in private attributes.
        """
        self.size = size
        self.position = position

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
            The new size value is validated
            to ensure it is a non-negative integer.
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

    @property
    def position(self):
        """
        Property: position
        Description: Retrieves the position of the square.

        Returns:
            tuple: The position of the square as a tuple of 2 integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position property.

        Args:
            value (tuple): The new position value to be set.

        Description:
            Sets the position of the square.
            The new position value is validated
            to ensure it is a tuple of 2 positive integers.
            If the value is valid,
            it is stored in the private __position attribute.

        Raises:
            TypeError: If the provided value is
            not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        with a length and width equal to the size, positioned according
        to the position attribute.
        """
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print the required number of newlines for the position
        for _ in range(self.__position[1]):
            print()

        # Print the square with the required number of spaces for the position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Method: __str__
        Description: Defines the string representation of the square.

        Returns:
            str: The string representation of the square,
            including the position and size.
        """
        square_str = ""
        if self.__size == 0:
            return square_str

        for _ in range(self.__position[1]):
            square_str += "\n"

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str[:-1]
