#!/usr/bin/python3
'''
    This the base class class of the entire
    project.
'''

import json


class Base:
    """
    A simple class to demonstrate object creation with automatic ID assignment.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
            number of objects created.
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation
        of a list of dictionaries.

        Parameters:
        - list_dictionaries (list): A list of dictionaries.

        Returns:
        - str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation
        of list_objs to a file using json.dump.

        Parameters:
        - list_objs (list): A list of instances inheriting from Base.

        Returns:
        - None

        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        js = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(js)
