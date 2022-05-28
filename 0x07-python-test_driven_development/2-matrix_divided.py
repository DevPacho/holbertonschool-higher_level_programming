#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Validations of variables for error handling."""

    new_matrix = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lists_inside in matrix:
        if type(lists_inside) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for numbers in lists_inside:
            if type(numbers) is not int and type(numbers) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists_inside in matrix:
        new_matrix.append(list(map(lambda to_div: round(to_div / div, 2), lists_inside)))

    return new_matrix
