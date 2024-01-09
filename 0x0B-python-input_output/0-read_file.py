#!/usr/bin/python3
'''
    Read text file in UTF-8
'''


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
