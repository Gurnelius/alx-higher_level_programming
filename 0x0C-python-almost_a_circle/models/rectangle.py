#!/usr/bin/python3
'''
    Rectangle class inheriting from
    Base class.
'''


from .base import Base


class Rectangle(Base):
    """
    A class representing a rectangle, inheriting from the Base class.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int): The x-coordinate of the top-left corner of the rectangle.
    - y (int): The y-coordinate of the top-left corner of the rectangle.
    - id (optional): An identifier for the rectangle.

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None):
        Initializes a Rectangle instance with the specified width, height,
        coordinates, and optional identifier.

    - height(self, value):
        Setter method for the height attribute.
        Raises TypeError if the input is not an integer,
        and ValueError if it is not greater than 0.

    - height(self):
        Getter method for the height attribute.

    - width(self, value):
        Setter method for the width attribute.
        Raises TypeError if the input is not an integer,
        and ValueError if it is not greater than 0.

    - width(self):
        Getter method for the width attribute.

    - x(self, value):
        Setter method for the x attribute.
        Raises TypeError if the input is not an integer,
        and ValueError if it is less than 0.

    - x(self):
        Getter method for the x attribute.

    - y(self, value):
        Setter method for the y attribute.
        Raises TypeError if the input is not an integer,
        and ValueError if it is less than 0.

    - y(self):
        Getter method for the y attribute.

    - area(self):
        Calculates and returns the area of the rectangle.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with the specified width, height,
        coordinates, and optional identifier.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the top-left
            corner of the rectangle (default is 0).
        - y (int, optional): The y-coordinate of the top-left
            corner of the rectangle (default is 0).
        - id (optional): An identifier for the rectangle.

        Returns:
        - None
        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        - int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        - value (int): The new value for the height attribute.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is not greater than 0.

        Returns:
        - None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        - int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        - value (int): The new value for the width attribute.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is not greater than 0.

        Returns:
        - None
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
        - int: The x-coordinate of the top-left corner of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Parameters:
        - value (int): The new value for the x attribute.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is less than 0.

        Returns:
        - None
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
        - int: The y-coordinate of the top-left corner of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Parameters:
        - value (int): The new value for the y attribute.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is less than 0.

        Returns:
        - None
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle using the character '#' and
        taking into account the x and y coordinates.

        Returns:
        - None
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string includes information about the rectangle's type,
        identifier (id), and the coordinates and dimensions of the rectangle.

        Returns:
            - str: A string representation of the Rectangle instance.

        """
        rect_rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
        return rect_rep

    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute of the Rectangle instance.

        This method accepts a variable number of positional arguments,
        where the order is crucial. The arguments are assigned to the
        corresponding attributes in the following order:

        1st argument: Assigns the value to the 'id' attribute.
        2nd argument: Assigns the value to the 'width' attribute.
        3rd argument: Assigns the value to the 'height' attribute.
        4th argument: Assigns the value to the 'x' attribute.
        5th argument: Assigns the value to the 'y' attribute.

        If **kwargs is provided, it assigns values based on the
        keys in the dictionary to the corresponding attributes.

        Parameters:
            - *args: Variable number of positional arguments.
                    The order of arguments is critical.
            - **kwargs: Variable number of keyword arguments (key-value pairs)

        Returns:
            - None
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
            Dictionary representation of Rectangle.

            Returns:
                - dict: A dictionary representation of the rectangle.
        '''
        rect_dict = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
            }
        return rect_dict
