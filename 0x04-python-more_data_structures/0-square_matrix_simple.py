#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [list(map(lambda a: a ** 2, a)) for a in matrix]
    return matrix2
