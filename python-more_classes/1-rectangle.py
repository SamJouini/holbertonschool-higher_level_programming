#!/usr/bin/python3
"Define a rectangle"


class Rectangle:
    "Initializes a Rectangle instance"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        "Retrieves the width of the rectangle."

        return self.__width
        "Returns:The width of the rectangle."

    @width.setter
    def width(self, value):
        "Sets the width of the rectangle."

        "TypeError: If the value is not an integer."
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        "ValueError: If the value is less than 0."
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Retrieves the height of the rectangle."

        return self.__height
        "Returns: The height of the rectangle."

    @height.setter
    def height(self, value):
        "Sets the height of the rectangle."

        "TypeError: If the value is not an integer."
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        "ValueError: If the value is less than 0."
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
