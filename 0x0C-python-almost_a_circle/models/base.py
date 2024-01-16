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

    @staticmethod
    def from_json_string(json_string="[]"):
        """
        Static method that returns a list of dictionaries
        from a JSON string representation.

        Parameters:
        - json_string (str): A JSON string.

        Returns:
        - list: A list of dictionaries.
        """
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that creates an instance with attributes set
        from a dictionary using the update method.

        Parameters:
        - **dictionary: A double pointer to a dictionary.

        Returns:
        - instance: An instance of the class with attributes set
        from the dictionary.

        Example:
        ```
        dictionary = {'id': 1, 'width': 3, 'height': 8}
        instance = Rectangle.create(**dictionary)
        print(instance)
        # Output: Rectangle instance with id=1, width=3, height=8
        ```
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1, 1, 1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1, 1, 1, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Class method that loads instances from a file in JSON format.

        Returns:
        - list: A list of instances.

        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.to_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
