#!/usr/bin/python3
'''
    Implement MyInt class with inverted
    equality operators
'''


class MyInt(int):
    """
    MyInt class, inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted.

    Example:
    >>> a = MyInt(3)
    >>> b = MyInt(3)
    >>> a == b
    False
    >>> a != b
    True
    """

    def __eq__(self, other_int):
        """
        Override the equality (==) operator.

        Parameters:
        - other_int: Any
            The object to compare with.

        Returns:
        - bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other_int)

    def __ne__(self, other_int):
        """
        Override the inequality (!=) operator.

        Parameters:
        - other_int: Any
            The object to compare with.

        Returns:
        - bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other_int)
