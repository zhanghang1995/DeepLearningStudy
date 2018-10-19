#!/usr/bin/python
# -*- coding: utf-8-*-
import os, sys
import math
import numpy as np

def basic_sigmoid(x):
    """
    Compute sigmoid of x

    Arguments:
    x -- A scalar

    :param x:
    :return:s = sigmoid(x)

    """

    ### start code here###
    s = 1/(1+1/np.exp(x))
    ### end code here###

    return s


if __name__  == '__main__':
    print(basic_sigmoid([1,2,3]))

    #事实上，我们很少在实际深度学习中很少使用math数学库，因为math库中我们输入的是常数，而在深度学习中我们使用的是矩阵或者向量。

