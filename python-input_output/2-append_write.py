#!/usr/bin/python3
"""
Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8 encoded)
    and returns the number of characters added.

    Args:
        filename (str): The path to the text file.
        If not provided, an empty string is used.
        text (str): The string to be appended to the file.
        If not provided, an empty string is used.

    Returns:
        int: The number of characters appended to the file.
    """
    if not filename:
        return 0

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
