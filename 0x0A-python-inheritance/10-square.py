#!/usr/bin/python3
'''
    Implement Square based off of the
    Rectangle class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Parameters:
    - size: int
        Size of the square.

    Methods:
    - area: Calculates the area of the square.

    Example:
    >>> square = Square(5)
    >>> square.area()
    25

    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Parameters:
        - size: int
            Size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is not a positive integer.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - str: String representation of the square.

        """
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
