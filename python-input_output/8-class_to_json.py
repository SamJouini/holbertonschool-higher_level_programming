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
    obj_dict = {}
    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
        else:
            obj_dict[attr] = str(value)
    return obj_dict