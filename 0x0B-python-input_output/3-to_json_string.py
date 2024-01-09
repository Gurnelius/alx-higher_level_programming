#!/usr/bin/python3
'''
    Represent string as JSON
'''


import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Parameters:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing
        the input object.
    """
    return json.dumps(my_obj)
