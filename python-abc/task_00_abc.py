#!/usr/bin/env python3
from abc import ABC, abstractmethod  
"Import the necessary components from the abc module"

class Animal(ABC):  
    "Define the abstract base class Animal that inherits from ABC"
    @abstractmethod  

    def sound(self):  
        "Declare an abstract method named sound"
        pass  
    "Abstract methods don't have an implementation in the base class"

class Dog(Animal):  
    "Define the concrete subclass Dog that inherits from Animal"
    def sound(self):  
        "Implement the sound method from the base class"
        return "Bark"  
    "Return the string Bark when the sound method is called on a Dog object"

class Cat(Animal):  
    "Define the concrete subclass Cat that inherits from Animal"
    def sound(self):  
        "Implement the sound method from the base class"
        return "Meow"  
    "Return the string Meow when the sound method is called on a Cat object"
