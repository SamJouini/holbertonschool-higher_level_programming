#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
