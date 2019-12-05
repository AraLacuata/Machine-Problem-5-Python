import numpy as np
import matplotlib.pyplot as plt
from math import *
n = np.linspace(0,199,200)
def sinfcn(x):
    y = np.zeros(200)
    for i in n:
        i = int(i)
        if i == 0:
            y[i] = -1.5*x[i] + 2*x[i+1] - 0.5*x[i+2]
        elif ((0 < i) and (i < 199)):
            y[i] = 0.5*x[i+1] - 0.5*x[i-1]
        elif i == 199:
            y[i] = 1.5*x[i] - 2*x[i-1] + 0.5*x[i-2]
    plt.plot(n,x,label = 'x(n)')
    plt.plot(n,y,label = 'y(n)')
    plt.legend()

## Initialize n & x = np.sin((3*pi*n)/100) in console, use x for machine problem test.