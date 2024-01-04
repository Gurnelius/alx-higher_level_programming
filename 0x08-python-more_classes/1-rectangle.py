#!/usr/bin/python3
'''
    Defines a rectangle.
'''


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width=0, height=0)
        Initializes a new Rectangle object with optional width and height.

        Parameters:
        - width (int): The width of the rectangle (default is 0).
        - height (int): The height of the rectangle (default is 0).

    Properties:
    - width
        Getter method to retrieve the width of the rectangle.
        Setter method to set the width of the rectangle.

    - height
        Getter method to retrieve the height of the rectangle.
        Setter method to set the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object with optional width and height.

        Parameters:
        - width (int): The width of the rectangle (default is 0).
        - height (int): The height of the rectangle (default is 0).
        """
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")

        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Parameters:
        - value (int): The height to set.

        Raises:
        - TypeError: If height is not an integer.
        - ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Parameters:
        - value (int): The width to set.

        Raises:
        - TypeError: If width is not an integer.
        - ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
