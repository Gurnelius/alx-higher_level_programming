#!/usr/bin/python3
'''
    Represent JSON string as Python Object
'''


import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Parameters:
        my_str (str): A JSON-formatted string to be
        converted to a Python object.

    Returns:
        Any: A Python object representing the data parsed
        from the input JSON string.
    """
    return json.loads(my_str)
