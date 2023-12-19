#!/usr/bin/python3

class Square:
    '''
    This is an empty class defining a square.

    Attributes:
        No attributes
    '''
    def __init__(self, size=0):
        '''
        Init method for the class.

        Args:
            size (int): Size of the square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
