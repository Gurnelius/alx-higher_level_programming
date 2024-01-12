#!usr/bin/python3
'''
    Square that inherits from Rectangle
'''


from .rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.

    Attributes:
    - size (int): The size of the square.
    - x (int): The x-coordinate of the top-left corner of the square.
    - y (int): The y-coordinate of the top-left corner of the square.
    - id (optional): An identifier for the square.

    Methods:
    - __init__(self, size, x=0, y=0, id=None):
        Initializes a Square instance with the specified size,
        coordinates, and optional identifier. Calls the super class with
        id, x, y, width, and height.

    - __str__(self):
        Returns a string representation of the Square instance.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance with the specified size, coordinates,
        and optional identifier.
        Calls the super class with id, x, y, width, and height.

        Parameters:
        - size (int): The size of the square.
        - x (int, optional): The x-coordinate of the top-left
            corner of the square (default is 0).
        - y (int, optional): The y-coordinate of the top-left
            corner of the square (default is 0).
        - id (optional): An identifier for the square.

        Returns:
        - None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        - str: A string representation of the Square instance.

        Example:
        ```
        square = Square(5, x=2, y=3, id=1)
        print(str(square))  # Output: "[Square] (1) 2/3 - 5"
        ```
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Assigns the value to both width and height.

        Parameters:
        - value (int): The new value for the size attribute.

        Raises:
        - TypeError: If the input is not an integer.
        - ValueError: If the input is not greater than 0.

        Returns:
        - None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes based on positional and
        key-value arguments.

        If *args is not empty, it assigns values based on the
        order of arguments:
            - 1st argument: Assigns the value to the 'id' attribute.
            - 2nd argument: Assigns the value to the 'size' attribute.
            - 3rd argument: Assigns the value to the 'x' attribute.
            - 4th argument: Assigns the value to the 'y' attribute.

        If **kwargs is provided, it assigns values based on the keys
        in the dictionary to the corresponding attributes.

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
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # Use **kwargs if *args is empty
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
            Dictionary representation of Square.

            Returns:
                - dict: A dictionary representation of the square.
        '''
        square_dict = {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y,
            }
        return square_dict
