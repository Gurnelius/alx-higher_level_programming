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
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object with optional width and height.

        Parameters:
        - width (int): The width of the rectangle (default is 0).
        - height (int): The height of the rectangle (default is 0).
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

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

    def area(self):
        """
        Getter method to retrieve the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Getter method to retrieve the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            rect = ""
        else:
            for h in range(self.__height):
                if h != self.__height - 1:
                    rect += "#" * self.__width + "\n"
                else:
                    rect += "#" * self.__width
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
