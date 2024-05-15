#!/usr/bin/python3
"Creates a square in Python."


class Square:
    "Defines a square with a private size attribute and validation."
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property   # Validate the position input
    def position(self):
        "Retrieves the position of the square"
        return self.__position

    @position.setter
    def position(self, value):
        "Check if the position is a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        "Calculates the area of the square."
        return self.__size ** 2
        "Returns: The area of the square."

    def my_print(self):
        "Prints the square using the '#' character."
        if self.__size == 0:
            "If the size is 0, print an empty line"
            print()
            return

        "Print the required number of newlines for the position"
        for _ in range(self.__position[1]):
            print()

        "Print the square with the required number of spaces for the position"
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        "Defines the string representation of the square."

        square_str = ""
        if self.__size == 0:
            return square_str

        for _ in range(self.__position[1]):
            square_str += "\n"

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str[:-1]
        "Returns: The string representation of the square."
