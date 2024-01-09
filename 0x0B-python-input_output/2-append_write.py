#!/usr/bin/python3
'''
 Append a string to text file
'''


def append_write(filename="", text=""):
    """
    Appends the specified text to the end of a
    text file.

    Parameters:
        filename (str): The name or path of the
            text file to which the text will be appended.
            Default is an empty string.
        text (str): The text content to be appended
            to the file. Default is an empty string.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
