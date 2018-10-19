# -*- coding:utf-8 -*-

"""
Calculates the softmax for each row of the input x
"""
import numpy as np

def sigmoid(x):
    """
    Your code should work fro a row vector and also fro matrices of shape(n,m)
    :param x: A numpy matrix of shape(n,m)
    :return: A numpy matrix equal to the softmax of x , of shape(n,m)


    """

    ### start code here ###
    x_exp = np.exp(x) #(n,m)

    #Create a vector x_sum that sums each row of x_exp
    x_sum = np.sum(x_exp,axis=1,keepdims=True)

    #Compute softmax(x) by dividing x_exp by x_sum.It should automatically use numpy broadcasting
    s = x_exp / x_sum
    return s


if __name__ == '__main__':
    x = np.array([
        [9,2,5,0,0],
        [7,5,0,0,0]
    ])
    print(sigmoid(x))