#!/usr/bin/env python3

from abc import ABC, abstractmethod
"Import the necessary components from the abc module"
import math


class Shape(ABC):
    "Define an abstract base class named Shape that inherits from ABC"
    @abstractmethod
    def area(self):
        """
        Declare an abstract method named area
        Abstract methods don't have an implementation in the base class
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Declare an abstract method named perimeter
        Abstract methods don't have an implementation in the base class
        """
        pass


class Circle(Shape):
    "Define a concrete subclass named Circle that inherits from Shape"
    def __init__(self, radius):
        """
        Constructor that takes a radius parameter
        Store the radius in an instance variable
        """
        self.radius = radius

    def area(self):
        """
        Implement the area method from the base class
        Calculate and return the area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Implement the perimeter method from the base class
        Calculate and return the perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    "Define a concrete subclass named Rectangle that inherits from Shape"
    def __init__(self, width, height):
        """
        Constructor that takes width and height parameters
        Store the width in an instance variable
        Store the height in an instance variable
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Implement the area method from the base class
        Calculate and return the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Implement the perimeter method from the base class
        Calculate and return the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    "Define a function named shape_info that takes a shape parameter"
    print("Area:", shape.area())
    """
    Call the area method of the shape object and print the result"
    Call the perimeter method
    """
    print("Perimeter:", shape.perimeter())
