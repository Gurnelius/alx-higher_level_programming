#!/usr/bin/python3

"""
Module: singly_linked_list

This module defines a singly linked list with two classes:
- Node: Represents a node in the singly linked list.
- SinglyLinkedList: Represents the singly linked list itself.

"""


class Node:
    """
    Node class represents a node in a singly linked list.

    Attributes:
        data (int): The data value of the node.
        next_node (Node): The next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Initializes a new
        instance of the Node class.
            Args:
                data (int): The data value of the node.
                next_node (Node, optional): The next node in the
                linked list. Default is None.

    Properties:
        data (int): Gets the data value of the node.
            Raises:
                TypeError: If the provided data is not an integer.
        next_node (Node): Gets the next node in the linked list.
            Raises:
                TypeError: If the provided next_node is not a Node object.

    """

    def __init__(self, data, next_node=None):
        pass

    @property
    def data(self):
        """
        Gets the data value of the node.

        Returns:
            int: The data value of the node.

        Raises:
            TypeError: If the data value is not an integer.
        """
        pass

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The new data value for the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        pass

    @property
    def next_node(self):
        """
        Gets the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        pass

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node for the current node.

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        pass


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.

    Attributes:
        head: The head of the linked list.

    Methods:
        __init__(self): Initializes a new instance of the
        SinglyLinkedList class.
        sorted_insert(self, value): Inserts a new Node into
        the correct sorted position in the list (increasing order).
            Args:
                value (int): The value to be inserted into the linked list.
        __str__(self): Returns a string representation of the linked list.

    """

    def __init__(self):
        pass

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The value to be inserted into the linked list.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        pass
