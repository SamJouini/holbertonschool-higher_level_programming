#!/usr/bin/python3
"""
Serialization module that adds the functionality
to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data dictionary
    and save it to the specified file in JSON format.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
