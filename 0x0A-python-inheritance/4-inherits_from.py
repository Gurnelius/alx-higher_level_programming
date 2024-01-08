#!/usr/bin/python3
'''
   Check if subclass of
'''


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False.

    Parameters:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
