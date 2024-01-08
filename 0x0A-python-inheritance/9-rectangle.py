#!/usr/bin/python3
'''
    Rectangle module implementation based on
    BaseGeometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.

    Parameters:
    - width: int
        Width of the rectangle.
    - height: int
        Height of the rectangle.

    Methods:
    - area: Calculates the area of the rectangle.

    Example:
    >>> rectangle = Rectangle(4, 5)
    >>> rectangle.area()
    20
    >>> print(rectangle)
    [Rectangle] 4/5
    >>> str(rectangle)
    '[Rectangle] 4/5'

    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Parameters:
        - width: int
            Width of the rectangle.
        - height: int
            Height of the rectangle.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is not a positive integer.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        - int: Area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - str: String representation of the rectangle.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
