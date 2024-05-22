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
