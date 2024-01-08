#!/usr/bin/python3
'''
    Get list of avaiiable attributes
    of an object.
'''


def lookup(obj):
    """
    Returns a list of attribute names and
    methods associated with the given object.

    Parameters:
        - obj: Any valid Python object
    Returns:
        - list: A list containing the names of
        attributes and methods of the input object.
    """
    return dir(obj)
