#!/usr/bin/python3
'''
'''


def class_to_json(obj):
    """
    Converts an instance of a class with serializable
    attributes into a dictionary for JSON serialization.

    Parameters:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object
        for JSON serialization.
    """
    dict_ = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            # Check if the attribute value is of a serializable type
            dict_[key] = value

    return dict_
