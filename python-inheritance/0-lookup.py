#!/usr/bin/python3


def lookup(obj):
    " Returns a list of available attributes and methods of an object."

    attributes = []
    for attr in dir(obj):
        try:
            value = getattr(obj, attr)
            if callable(value):
                attributes.append(f"{attr}()")
            else:
                attributes.append(attr)
        except AttributeError:
            pass
    return attributes
