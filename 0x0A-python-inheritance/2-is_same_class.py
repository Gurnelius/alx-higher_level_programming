#!/usr/bin/python3
'''
    This module checks if an object
    is exactly an instance of specified
    class.
'''


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of the specified class; otherwise False.

    Parameters:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if the object is an instance of the
    specified class; otherwise False.

    Example:
    >>> is_same_class(5, int)
    True
    """
    return type(obj) is a_class
