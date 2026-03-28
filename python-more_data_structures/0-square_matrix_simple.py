#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newone = []
    for row in matrix:
        newrow = []
        for i in row:
            newrow.append(i ** 2)
        newone.append(newrow)
    return newone
