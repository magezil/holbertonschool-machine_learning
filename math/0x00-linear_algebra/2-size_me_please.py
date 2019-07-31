#!/usr/bin/env python3


def matrix_shape(matrix):
    """
        Calculates the shape of given matrix
        matrix: matrix to calculate

        Return: list of ints
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])