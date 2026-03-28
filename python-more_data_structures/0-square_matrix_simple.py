#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newone=[]
    for row in matrix:
        newrow=[]
        for i in row:
            j=i**2
            newrow.append(j)
        newone.append(newrow)
        print('\n')
    return(newone)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
