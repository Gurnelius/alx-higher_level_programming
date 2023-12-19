#!/usr/bin/python3

''' Define a Square class'''


class Square:
    '''
    This is a class defining a square.

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

    def area(self):
        '''
        Calculate the area of the square
        Args:
            None
        Returns:
            int: area of the square
        '''
        return self.__size * self.__size
