#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of the characters: ., ? and :"""


def text_indentation(text):
    "TypeError: If text is not a string."
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in characters:
            new_text += "\n\n"

    lines = new_text.split("\n")
    for line in lines:
        print(line.strip())
