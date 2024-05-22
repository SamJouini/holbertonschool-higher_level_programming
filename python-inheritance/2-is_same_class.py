#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class, False otherwise.
    """

    return type(obj) is a_class
    """
    Returns: True if the object is exactly an instance
    of the specified class, False otherwise.
    """
