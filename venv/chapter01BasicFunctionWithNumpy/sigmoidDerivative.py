#!/usr/bin/python
# -*- coding: utf-8-*-

import numpy as np


def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.

    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """

    ### start code here###
    s = 1/(1+1/np.exp(x))
    ds = s*(1-s)
    ### end code here###

    return ds


if __name__ == "__main__":
    print(sigmoid_derivative([1,2,3,4]))
