#!/usr/bin/python3
" Returns a list of available attributes and methods of an object."


def lookup(obj):
    "obj: The object to inspect."

    attributes = []
    for attr in dir(obj):
        try:
            value = getattr(obj, attr)
            if callable(value):
                attributes.append(f"{attr}")
            else:
                attributes.append(attr)
        except AttributeError:
            pass
    return attributes
    " Returns: A list containing the names of available attributes and methods."