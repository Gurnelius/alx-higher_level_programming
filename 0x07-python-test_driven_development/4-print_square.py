#!/usr/bin/python3
'''
    Module to print a sqaure with
    the character #.
'''


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not isinstance(size, int) and size < 0:
        raise TypeError("size must be and integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
