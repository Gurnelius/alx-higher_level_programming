#!/usr/bin/python3

'''
    This module contains only one function]
    t add two integers
'''


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int): The first integer to be added.
    - b (int, optional): The second integer to be added. Default is 98.

    Returns:
    int: The sum of the two input integers.

    Example:
    >>> add_integer(5, 3)
    8

    >>> add_integer(10)
    108
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
