#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to stdout.

    Args:
        filename (str): The path to the text file.
        If not provided, an empty string is used.
    """
    if not filename:
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print("Error: {}".format(e))
