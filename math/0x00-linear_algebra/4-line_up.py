#!/usr/bin/python3


def add_arrays(arr1, arr2):
    """ 
        Add two arrays element-wise
        arr1: list of ints/floats
        arr2: list of ints/floats
        
        Return: list of ints/floats or None if arrays are not same shape
    """
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None

def matrix_shape(matrix):
    """
        Calculates the shape of given matrix
        matrix: matrix to calculate

        Return: list of ints
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])
