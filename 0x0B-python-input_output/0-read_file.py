#!/usr/bin/python3
'''
    Read text file in UTF-8
'''


def read_file(filename=""):
    """
    Reads the contents of a text file and prints
    it to the console.

    Parameters:
        filename (str): The name or path of the
        text file to be read. Default is an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
