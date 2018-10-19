# -*- coding:utf-8 -*-

def gradient(x,y):
    theart0 = 0
    theart1 = 0
    # learning rate define 0.5
    learningRate = 0.01
    for i in range(100000):
        sum0 = 0
        sum1 = 0
        for j in range(len(x)):
            print(len(x))
            sum0 += theart0 + theart1*x[j] - y[j] #从1加到m
            print(sum0)
            sum1 += (theart0 + theart1 * x[j] - y[j])*x[j]  # 从1加到m
            print(sum1)
        temp0 = theart0 - learningRate*(1/len(x))*sum0
        print(temp0)
        temp1 = theart1 - learningRate*(1/len(x))*sum1
        print(temp1)
        theart0 = temp0
        theart1 = temp1
    return theart1,theart0

if __name__ == '__main__':
    x = [1,2,2,3,3,4,5,6,6,6,8,10]
    y = [-890,-1411,-1560,-2220,-2091,-2878,-3537,-3268,-3920,-4163,-5471,-5157]
    print(gradient(x,y))