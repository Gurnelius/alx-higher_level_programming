#!/usr/bin/python3
'''
    Module to print name
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints a formatted string with the provided
    first and last names.

    Parameters:
        - first_name (str): The first name to be
        included in the formatted string.
        - last_name (str, optional): The last name to
        be included in the formatted string.
        Default is an empty string.

    Raises:
        - TypeError: If `first_name` is not a string
        or if `last_name` is not a string.

    Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe

    >>> say_my_name("Alice")
    My name is Alice
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
