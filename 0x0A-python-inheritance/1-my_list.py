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
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
