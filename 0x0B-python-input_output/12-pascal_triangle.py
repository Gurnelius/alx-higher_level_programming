#!/usr/bin/python3
'''
    This module implements Pascal's Truangle.
    It returns a list of lists of integers representing
    the Pascal’s triangle of n
'''


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Parameters:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Note:
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.extend([prev_row[j] + prev_row[j + 1]])
            row.append(1)
        triangle.append(row)

    return triangle
