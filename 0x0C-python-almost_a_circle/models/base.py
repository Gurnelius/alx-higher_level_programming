#!/usr/bin/python3
'''
    This the base class class of the entire
    project.
'''


class Base:
    """
    A simple class to demonstrate object creation with automatic ID assignment.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.
        id (int): A public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An integer representing the ID.
            If provided, assigns this value to the id attribute.
            If not provided, increments the __nb_objects counter
            and assigns the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
