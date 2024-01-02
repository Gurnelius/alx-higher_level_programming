#!/usr/bin/python3
'''
    Module has only one function
    matrix_divided that divides all
    elements in the matrix.
'''


def matrix_divided(matrix, div):
    '''
        Divides all elements in matrix by
        div

        Parameters:
            - matrix (list): contain elements (int or float)
                of the matrix.
            - div (int or float): number to divide matrix by.
        Return:
            list: new matrix after division.
    '''

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err)

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        raise TypeError(err)

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element/div, 2) for element in row] for row in matrix]
