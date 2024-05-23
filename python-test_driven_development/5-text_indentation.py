#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of the characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`.

    Args:
    text : The input text to be print.

    Raises:
    TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in characters:
            new_text += "\n"

    lines = new_text.split("\n\n")
    for line in lines:
        print(line.strip(), end='')
