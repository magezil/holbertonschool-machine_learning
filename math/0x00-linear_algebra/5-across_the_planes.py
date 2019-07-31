#!/usr/bin/env python3
"""Implement add_matrices2D function"""


def add_matrices2D(mat1, mat2):
    """
        Add two matrices element-wise

        Return: Return new matrix or
                None if two matrices are not the same shape
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    sum_matrix = []
    for row1, row2 in zip(mat1, mat2):
        sum_matrix.append([])
        for x, y in zip(row1, row2):
            sum_matrix[-1].append(x + y)
    return sum_matrix


def matrix_shape(matrix):
    """
        Calculates the shape of given matrix
        matrix: matrix to calculate

        Return: list of ints
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])
