#!/usr/bin/python3
'''
    Represent JSON string as Python Object
'''


import json


def from_json_string(my_str):
    return json.loads(my_str)