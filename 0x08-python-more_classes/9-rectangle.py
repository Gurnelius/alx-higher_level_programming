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
    print_symbol = "#"

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two Rectangle instances and return
        the one with the equal or greater area.

        Parameters:
            rect_1 (Rectangle): The first rectangle instance for comparison.
            rect_2 (Rectangle): The second rectangle instance for comparison.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of the
            Rectangle class.

        Returns:
            Rectangle: The larger or equal Rectangle instance based on area.

        Example:
            # Create two rectangles
            rect1 = Rectangle(4, 5)
            rect2 = Rectangle(3, 6)

            # Get the larger or equal rectangle
            larger_rect = Rectangle.bigger_or_equal(rect1, rect2)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new instance of the Rectangle
        class representing a square.

        Parameters:
            cls (class): The class itself.
            size (int, optional): The size of the square.
            Defaults to 0.

        Returns:
            Rectangle: A new instance of the Rectangle class
            with equal width and height, representing a square.

        Example:
            # Create a square with size 5
            square_instance = Rectangle.square(5)
        """
        return cls(size, size)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: A string representation of the rectangle using
            the print_symbol character.
        Example:
            # Create a rectangle and get its string representation
            rectangle_instance = Rectangle(3, 4)
            print(str(rectangle_instance))
        """
        rect = ""
        self.print_symbol = str(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            rect = ""
        else:
            for h in range(self.__height):
                if h != self.__height - 1:
                    rect += self.print_symbol * self.__width + "\n"
                else:
                    rect += self.print_symbol * self.__width
        return rect

    def __repr__(self):
        """
        Return a string representation of the Rectangle
        instance for recreation using eval().

        Returns:
            str: A string representation of the rectangle
            in the format 'Rectangle(width, height)'.

        Example:
            # Create a rectangle and get its string
            representation for recreation
            rectangle_instance = Rectangle(3, 4)
            repr_string = repr(rectangle_instance)
            new_instance = eval(repr_string)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method to decrement the number_of_instances
        attribute and print a farewell message.

        Example:
            # Delete a rectangle instance
            del rectangle_instance
            # Output: Bye rectangle...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
