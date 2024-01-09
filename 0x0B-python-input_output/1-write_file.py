#!/usr/bin/python3
'''
 Write a string to text file
'''


def write_file(filename="", text=""):
    """
    Writes the specified text to a text file.

    Parameters:
        - filename (str): The name or path of the
            text file to be written. Default is an
            empty string.
        - text (str): The text content to be written
            to the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.
`   """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
