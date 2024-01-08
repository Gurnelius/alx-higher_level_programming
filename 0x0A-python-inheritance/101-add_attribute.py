#!/usr/bin/python3
'''
    Add new attribute to an object
    if possible.
'''


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: object
        The object to which the attribute should be added.
    - name: str
        The name of the new attribute.
    - value: any
        The value of the new attribute.

    Raises:
    - TypeError: If the object cannot have a new attribute.

    Example:
    >>> class Example:
    ...     pass
    >>> obj = Example()
    >>> add_attribute(obj, "new_attr", 42)
    >>> print(obj.new_attr)
    42

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
