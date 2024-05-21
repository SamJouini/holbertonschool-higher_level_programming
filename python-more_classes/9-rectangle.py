#!/usr/bin/python3
"Define a rectangle"


class Rectangle:
    "Initializes a Rectangle instance"
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        "Calculates the area of the rectangle."

        return self.width * self.height
        "Returns: The area of the rectangle."

    def perimeter(self):
        "Calculates the perimeter of the rectangle."

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
        """
        Returns:The perimeter of the rectangle.
        If either width or height is 0, returns 0.
        """

    def __str__(self):
        """
        Returns a string representation
        of the rectangle using the character '#'.
        """

        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str.rstrip()
        "Returns: The string representation of the rectangle."

    def __repr__(self):
        """"
        Returns a string representation of the rectangle
        that can be used to recreate a new instance.
        """

        return f"Rectangle({self.width}, {self.height})"
        "Returns: The string representation of the rectangle."

    def __del__(self):
        " rints a message when an instance of Rectangle is deleted."
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        "Returns the biggest rectangle based on the area."

        "TypeError: If rect_1 or rect_2 is not an instance of Rectangle."
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
            """
            Returns: The biggest rectangle based on the area,
            or rect_1 if both have the same area.
            """
    @classmethod
    def square(cls, size=0):
        "Returns a new Rectangle instance with width == height == size."

        return cls(size, size)
        "Returns: A new Rectangle instance with width == height == size."
