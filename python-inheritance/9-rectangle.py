#!/usr/bin/python3
"""
A base class for geometry-related classes.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Calculates the area of a geometric shape."

    def __init__(self, width, height):
        "Initializes a Rectangle object with the given width and height."

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        "Calculates and returns the area of the rectangle."
        return self.__width * self.__height

    def __str__(self):
        "Returns a string representation of the rectangle."
        return f"[Rectangle] {self.__width}/{self.__height}"
