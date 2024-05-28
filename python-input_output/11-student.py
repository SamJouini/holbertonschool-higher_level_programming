#!/usr/bin/python3
"Write a class Student that defines a student"


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to be retrieved.
                If provided, only the specified attributes
                will be included in the dictionary.
                If not provided or None, all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                'last_name': self.last_name,
                'first_name': self.first_name,
                'age': self.age
            }
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
            instance with values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names
            and their corresponding values.
        """
    for attr, value in json.items():
        if hasattr(self, attr):
            setattr(self, attr, value)
