#!/usr/bin/env python3


class SwimMixin:
    "Creating the SwimMixin class"
    def swim(self):
        print("The creature swims!")


"""
The SwimMixin class has a single method 'swim'
that prints "The creature swims!"
This mixin encapsulates the behavior of swimming.
"""


class FlyMixin:
    "Creating the FlyMixin class"
    def fly(self):
        print("The creature flies!")


"""The FlyMixin class has a single method 'fly'
that prints "The creature flies!"
This mixin encapsulates the behavior of flying.
"""


class Dragon(SwimMixin, FlyMixin):
    "Implementing the Dragon class"
    def roar(self):
        print("The dragon roars!")


"""
The Dragon class inherits from both SwimMixin and FlyMixin.
By inheriting from these mixins, the Dragon class
automatically gains the 'swim' and 'fly' methods.
"""
