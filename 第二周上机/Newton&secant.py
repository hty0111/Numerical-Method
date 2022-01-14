from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    y = x * float(tan(x)) - 2
    return y

def df(x):
    dy = float(tan(x)) + x/(float(cos(x))**2)
    return dy

#initialize arrays for visualization
axis_x_1 = []
axis_x_2 = []
axis_y_1 = []
axis_y_2 = []

#Newton
x2 = float(pi/2-0.001)
x1 = 0.001
tolerance = 0.0001
n = 0

while (abs((x2-x1)/x2) > tolerance):
    x1 = x2
    x2 = x1-f(x1)/df(x1)
    
    if f(x2) < 200:
        axis_x_1.append(x2)
        axis_y_1.append(f(x2))
    
    n += 1

print('The result of Newton method is %.8f, times of looping is %d' % (x2, n))


#secant
px1 = float(pi/2-0.001)
px2 = 0.001
tolerance = 0.0001
n = 0

while (abs((px2-px1)/px2)>tolerance):
    px3 = px2 - f(px2) * (px2-px1) / (f(px2)-f(px1))
    if f(px2)*f(px1) > 0:
        if (abs(px2)-abs(px3)) < (abs(px1)-abs(px3)):
            px1 = px3
        else:
            px2 = px3
    else:
        if f(px3)*f(px2) > 0:
            px1 = px3
        else:
            px2 = px3

    if abs(px3) < 5:
        axis_x_2.append(px3)
        axis_y_2.append(f(px3))
    
    n += 1
x = abs(px3)

print('The result of secant method is %.8f, times of looping is %d' % (x, n))

plt.scatter(axis_x_1, axis_y_1, label='Newton')
plt.scatter(axis_x_2, axis_y_2, label='secant')
plt.legend()
plt.show()
