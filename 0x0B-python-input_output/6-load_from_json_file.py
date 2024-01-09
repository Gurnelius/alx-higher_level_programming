#!/usr/bin/python3
'''
    Create object from JSON file
'''


import json

def load_from_json_file(filename):
    """
    Loads data from a JSON file and returns the
    corresponding Python object.

    Parameters:
        filename (str): The name or path of the
        JSON file to be loaded.
    Returns:
        Any: A Python object representing the data stored
        in the JSON file.
    """
    with open(filename, 'r') as file:
        var = json.load(file)
    return var
