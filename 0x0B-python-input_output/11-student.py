#!/usr/bin/python3
'''
    Implement student class. Set attributes from
    json.
'''


class Student:
    """
    Class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list, optional): A list of strings representing
            attribute names to be retrieved.
            If None, all attributes are retrieved. Default is None.

        Returns:
            dict: A dictionary containing the specified attributes
            of the Student instance.
        """
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            # Only retrieve specified attributes from the list
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based
        on the provided dictionary.

        Parameters:
            json (dict): A dictionary where keys are attribute
            names and values are attribute values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
