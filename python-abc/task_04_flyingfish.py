#!/usr/bin/env python3

class Fish:
    "Define the swim method for the Fish class"
    def swim(self):
        "This method prints The fish is swimming"
        print("The fish is swimming")

    def habitat(self):
        "Define the habitat method for the Fish class"
        print("The fish lives in water")
        "This method prints The fish lives in water"


class Bird:
    def fly(self):
        "Define the fly method for the Bird class"
        print("The bird is flying")
        "This method prints The bird is flying"

    def habitat(self):
        "Define the habitat method for the Bird class"
        print("The bird lives in the sky")
        "This method prints The bird lives in the sky"


class FlyingFish(Fish, Bird):
    """
    The FlyingFish class inherits from both Fish and Bird
    The order of inheritance matters for method resolution order (MRO)
    """

    def fly(self):
        "Override the fly method from the Bird class"
        print("The flying fish is soaring!")
        "This method prints The flying fish is soaring!"

    def swim(self):
        "Override the swim method from the Fish class"
        print("The flying fish is swimming!")
        "This method prints The flying fish is swimming!"

    def habitat(self):
        "Override the habitat method from both Fish and Bird classes"
        print("The flying fish lives both in water and the sky!")
        "This method prints The flying fish lives both in water and the sky!"
