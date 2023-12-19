#!/usr/bin/python3

''' Define a Square class.'''


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

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square.
                Default is 0.
            position (tuple): position of the square
        '''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''
        Gets the position of the square.
        Returns:
            tuple: The position of the square.
        '''
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        '''
        Sets the position of the square.
        Args:
            position (tuple, optional): New position for the square.
            Default is (0, 0)
        Raises:
            TypeError: If the provided value is not a tuple or does
            not contain 2 positive integers.
        '''
        is_tuple = isinstance(position, tuple)
        len_2 = len(position) != 2
        is_int = all(isinstance(i, int) for i in position)

        if not is_tuple or len_2 or not is_int:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
        Prints the square pattern using the '#' character.

        If the size is equal to 0, it prints an empty line.
        The position is used by adding spaces before printing '#' characters.

        Returns:
            None
        '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
