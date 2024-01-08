#!/usr/bin/python3
'''
    Module to implement BaseGeometry class
'''


class BaseGeometry:
    '''
        BaseGeometry class
        Methods:
            -area: not implemented
            -integer_validator: check for integer values
    '''
    def area(self):
        '''
            Area method.
            Parameters:
                -None
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value for a specified variable name.

        Parameters:
            - name: str
                The name of the variable being validated.
            - value: int
                The value to be validated.
        Raises:
            - TypeError: If the provided value is not an integer.
            - ValueError: If the provided integer value is less
            than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
