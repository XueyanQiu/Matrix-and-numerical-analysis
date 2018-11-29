from numpy import *
from matplotlib import pyplot as plt
import math

def f(x):
    return x*(math.e)**x-1

def f_derivative(x):
    return (math.e)**x+x*(math.e)**x

def newton():
    x0 = 0.5
    x1 = 0.6
    count = 0
    while True:
        x0 = x1
        f_derivative_num = f_derivative(x0)
        if f_derivative_num != 0:
            x1 = x0 - f(x0) / f_derivative_num
        else:
            return
        if abs(x1 - x0) < 1e-10:
            break
        else:
            print 'Newton:',count
            print abs(x1 - x0)
            count += 1
    return x1

def secant():
    x0 = 0.5
    x1 = 0.6
    count = 0
    while True:       
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print 'Secant:',count,x2
        print abs(x2 - x1)
        if abs(x2-x1) < 1e-5:             
            break
        else:
           
            x0 = x1
            x1 = x2
            count += 1
    return x2

if __name__ == '__main__':
    ans1 = newton()
    ans2 = secant()

    x = linspace(-5,5,1000)
    y = f(x)
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.plot(x,y,color='r',linestyle='-',label='f(x)')
    ax.scatter(ans1,f(ans1),label='Newton',color='y')
    ax.scatter(ans2,f(ans2),label='Secant',color='k')
    ax.legend(loc='lower right')
    fig.show()
    fig.savefig('a.png')
