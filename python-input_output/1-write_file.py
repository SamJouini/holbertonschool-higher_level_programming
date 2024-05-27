#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded)
    and returns the number of characters written.

    Args:
        filename (str): The path to the text file.
        If not provided, an empty string is used.
        text (str): The string to be written to the file.
        If not provided, an empty string is used.

    Returns:
        int: The number of characters written to the file.
    """
    if not filename:
        return 0

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
