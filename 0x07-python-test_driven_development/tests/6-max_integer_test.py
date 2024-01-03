#!/usr/bin/python3
'''
    Module to test max_integer function
'''

import unittest

class TestMaxInteger(unittest.TestCase):
    '''
    Test class for the max_integer function.

    Attributes:
        - None

    Methods:
        - test_max_integer: Tests the max_integer function
        with various scenarios.
    '''

    def test_max_integer(self):
        '''
        Tests the max_integer function with various scenarios.

        Scenario 1: List with positive integers.
        - Input: [1, 2, 3, 5]
        - Expected Output: 5

        Scenario 2: List with negative integers.
        - Input: [-4, -3, -8, -7]
        - Expected Output: -3

        Scenario 3: List with a single element.
        - Input: [3]
        - Expected Output: 3

        Scenario 4: Empty list.
        - Input: []
        - Expected Output: None
        '''
        max_integer = __import__("6-max_integer").max_integer

        # Scenario 1
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

        # Scenario 2
        self.assertEqual(max_integer([-4, -3, -8, -7]), -3)

        # Scenario 3
        self.assertEqual(max_integer([3]), 3)

        # Scenario 4: Empty list
        self.assertIsNone(max_integer([]))
