#!/usr/bin/python3
'''
 Append a string to text file
'''


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
