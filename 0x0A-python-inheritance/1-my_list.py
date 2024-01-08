#!/usr/bin/python3
'''
    Module that sorts items in a list.
'''


class MyList(list):
    """
    A custom list class that inherits from the
    built-in list class.

    Public instance method:
    - print_sorted(self): Prints the list in
    ascending sorted order.

    Example:
    >>> my_list = MyList([5, 2, 7, 1, 10])
    >>> my_list.print_sorted()
    [1, 2, 5, 7, 10]
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Example:
        >>> my_list = MyList([4, 2, 1])
        >>> my_list.print_sorted()
        [1, 2, 4]
        """
        sorted_list = sorted(self)
        print(sorted_list)
