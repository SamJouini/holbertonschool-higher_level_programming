#!/usr/bin/python3
""""
Function that returns the JSON representation of an object (Python data structure).
"""

import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object (Python data structure).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_str)
