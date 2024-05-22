#!/usr/bin/env python3

from abc import ABC, abstractmethod
"Import the necessary components from the abc module"
import math


class Shape(ABC):
    "Define an abstract base class named Shape that inherits from ABC"
    @abstractmethod
    def area(self):
        "Declare an abstract method named area"
        pass
    "Abstract methods don't have an implementation in the base class"

    @abstractmethod
    def perimeter(self):
        "Declare an abstract method named perimeter"
        pass
    "Abstract methods don't have an implementation in the base class"


class Circle(Shape):
    "Define a concrete subclass named Circle that inherits from Shape"
    def __init__(self, radius):
        "Constructor that takes a radius parameter"
        self.radius = radius
        "Store the radius in an instance variable"

    def area(self):
        "Implement the area method from the base class"
        return math.pi * self.radius ** 2
    "Calculate and return the area of the circle"

    def perimeter(self):
        "Implement the perimeter method from the base class"
        return 2 * math.pi * self.radius
    "Calculate and return the perimeter of the circle"


class Rectangle(Shape):
    "Define a concrete subclass named Rectangle that inherits from Shape"
    def __init__(self, width, height):
        "Constructor that takes width and height parameters"
        self.width = width
        "Store the width in an instance variable"
        self.height = height
        "Store the height in an instance variable"

    def area(self):
        "Implement the area method from the base class"
        return self.width * self.height
    "Calculate and return the area of the rectangle"

    def perimeter(self):
        "Implement the perimeter method from the base class"
        return 2 * (self.width + self.height)
    "Calculate and return the perimeter of the rectangle"


def shape_info(shape):
    "Define a function named shape_info that takes a shape parameter"
    print("Area:", shape.area())
    "Call the area method of the shape object and print the result"
    print("Perimeter:", shape.perimeter())
    "Call the perimeter method"
