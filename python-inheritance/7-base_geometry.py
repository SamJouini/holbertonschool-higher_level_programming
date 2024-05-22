#!/usr/bin/python3
"""
A base class for geometry-related classes.
"""


class BaseGeometry:
    "Calculates the area of a geometric shape."

    def area(self):

        raise Exception("area() is not implemented")
        """
        Raises an Exception with the message "area() is not implemented".
        """

    def integer_validator(self, name, value):
        "Validates if the given value is a positive integer."

        """
        TypeError: If value is not an integer,
        with the message <name> must be an integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        """
        ValueError: If value is less than or equal to 0,
        with the message <name> must be greater than 0.
        """
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
