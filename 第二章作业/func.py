import math
import sympy
import numpy as np
import matplotlib.pyplot as plt

Ta = sympy.Symbol('Ta')
fx = Ta/10 * (sympy.cosh(500/Ta) - 1) - 10
dfx = sympy.diff(fx, Ta)

#return the value of 'f(x)'
def f(x):
    return x/10 * (sympy.cosh(500/x) - 1) - 10

#return the dirivative value of 'f(x)'
def df(x):
    return dfx.evalf(subs={Ta:x})
