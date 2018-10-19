# -*-coding: utf-8-*-
"""
 It often leads to a better performance because gradient descent converges faster after normalization.
 Here, by normalization we mean changing x to x∥x∥
 (dividing each row vector of x by its norm).

 Exercise: Implement normalizeRows() to normalize the rows of a matrix.
 After applying this function to an input matrix x, each row of x should be a vector of unit length (meaning length 1).
"""
import numpy as np

def normaizeRows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length)
    :param x: A numpy matrix of shape(n,m)
    :return: The normalized (by row) numpy matrix. You are allowed to modify x.
    """

    ### start coding here###
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, axis = 1, keepdims = True) #计算每一行的长度，得到一个列向量
    # Divide x by its norm
    x = x / x_norm
    ### end coding here###

    return x

if __name__  == '__main__':
    x = np.array([
        [0, 3, 4],
        [1, 6, 4]])

    print("normalizeRows(x) = " ,str(normaizeRows(x)))
