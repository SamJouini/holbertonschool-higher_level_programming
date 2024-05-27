#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The path to the text file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
