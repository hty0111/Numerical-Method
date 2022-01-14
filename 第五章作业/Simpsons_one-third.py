import numpy as np
import sympy as sp
import math

x = sp.Symbol("x")
f = 2*math.pi*x*10*sp.root((1-x/0.75), 7)
xValue = np.array([0, 0.75])
d = 0.75            #区间长度
delta = 1e-8        #微小偏移量

def simpsons(xValue, f):
    fx0 = f.evalf(subs={x: xValue[0]})
    fx1 = f.evalf(subs={x: (xValue[1]+xValue[0])/2})
    fx2 = f.evalf(subs={x: xValue[1]})
    result = d*(fx0+4*fx1+fx2)/6
    return result

result = simpsons(xValue, f)

Real = sp.integrate(f, (x, xValue[0], xValue[1]-delta)).evalf()    #计算真值
Et = abs(Real - result)                 #计算绝对误差
epsilon = Et / Real * 100               #计算相对误差

print("result = %.10f, Et = %.10f, epsilon = %.2f%%" % (result, Et, epsilon))

