#!/usr/bin/python3
"""
function that divides all elements of a matrix.
div must be a number (integer or float), otherwise raise a TypeError exception.
Returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats, otherwise is error.
    """

    new_mx = []
    Mx_TypeError = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(Mx_TypeError)
    if matrix is None and matrix[0] is None:
        raise TypeError(Mx_TypeError)
    if type(matrix) is not list:
        raise TypeError(Mx_TypeError)
    for lists_inside in matrix:
        if type(lists_inside) is not list:
            raise TypeError(Mx_TypeError)
        for numbers in lists_inside:
            if type(numbers) is not int and type(numbers) is not float:
                raise TypeError(Mx_TypeError)

    if not all(len(lists_inside) is len(matrix[0]) for lists_inside in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists_inside in matrix:
        new_mx.append(list(map(lambda dv: round(dv / div, 2), lists_inside)))

    return new_mx
