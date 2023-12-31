#!/usr/bin/python3

''' Define Square class.'''


class Square:
    '''
    This class defines a square.

    Attributes:
        No public attributes

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
        area(self): Calculates and returns the area of the square.
    '''

    def __init__(self, size=0):
        '''
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square.
                Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''
        Gets the size of the square.

        Returns:
            int: The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square.

        Args:
            value (int): New size for the square.
        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        '''
        return self.__size * self.__size
