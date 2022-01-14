import sympy as sp

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
xValue = [0, 0.75]
delta = 1e-10
j = 4
k = 4

def trapezoidal(x0, x1, f):
    fx0 = f.evalf(subs={x: x0})
    fx1 = f.evalf(subs={x: x1})
    result = (x1-x0)*(fx0+fx1)/2
    return result

def romberg(j, k):        #根据定义推导龙贝格公式
    if k > 1:
        result = (1/(4**(k-1)-1))*(4**(k-1)*romberg(j, k-1) - romberg(j-1, k-1))
    else:
        h = (xValue[1]-xValue[0])/(2**(j-1))
        x = xValue[0]
        count = 0
        result = 0
        while count < 2**(j-1):
            result += trapezoidal(x, x+h, f)
            x += h
            count += 1
    return result

result = romberg(j, k)
Real = sp.integrate(f, (x, xValue[0], xValue[1]-delta)).evalf()    #计算真值
Et = abs(Real - result)                 #计算绝对误差
epsilon = Et / Real * 100               #计算相对误差

print("result = %.10f, Et = %.10f, epsilon = %.4f%%" % (result, Et, epsilon))
