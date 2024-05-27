#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    for JSON serialization of an object.
    
    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
