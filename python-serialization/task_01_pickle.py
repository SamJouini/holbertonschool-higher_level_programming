#!/usr/bin/python3
"""
Basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and
deserialize the JSON file to recreate the Python Dictionary.
"""
import pickle
import json


class CustomObject:
    """
    A custom class representing an object with name, age, and student status.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object is a student or not.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted string.
        """
        print("Name: {0}".format(self.name))
        print("Age: {0}".format(self.age))
        print("Is Student: {0}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save the serialized object.

        Returns:
            None: If an exception occurs during serialization.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error serializing object: {0}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file
            containing the serialized object.

        Returns:
            CustomObject: The deserialized object,
            or None if an exception occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print("Error deserializing object: {0}".format(e))
            return None
