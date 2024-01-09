#!/usr/bin/python3
'''
    Save object to file
'''


import json


def save_to_json_file(my_obj, filename):
    '''
        Save Python object to file using
        JSON representation.

        Parameters:
            my_obj: python object
            filename (str): file name
        Return:
            None
    '''
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
