#!/usr/bin/env python3
"""Implement cat_matrices2D function"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        Concatenate two matrices along a given axis

        Return: new matrix or none if two matrices are of different shapes
    """
    new_mat = []
    if axis == 0:
        for row in mat1:
            new_mat.append(list(row))
        for row in mat2:
            new_mat.append(list(row))
    if axis == 1:
        for row, element in zip(mat1, mat2):
            new_mat.append(list(row) + element)
    return new_mat
