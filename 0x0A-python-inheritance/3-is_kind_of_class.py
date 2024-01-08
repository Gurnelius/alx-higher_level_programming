#!/usr/bin/python3
'''
    This module checks if an object
    is exactly an instance of, or if
    the object is an instance of a class
    that inherited from, the specified class.
'''


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of, or if the object is an instance
    of a class that inherited from, the specified class;
    otherwise False.

    Parameters:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if the object is an instance of the
    specified class; otherwise False.

    Example:
    >>> is_kind_of_class(5, int)
    True
    """
    return isinstance(obj, a_class)
