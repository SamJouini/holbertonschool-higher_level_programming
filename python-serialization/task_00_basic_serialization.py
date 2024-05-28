#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data dictionary
    and save it to the specified file in JSON format.

    Args:
        data (dict): A Python dictionary containing the data to be serialized.
        filename (str): The filename of the output JSON file.
        If the file already exists, it will be replaced.
    """

    with open(filename, 'w') as file:
        json.dumps(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary containing
        the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
