import sympy as sp

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
d = 0.75    #区间长度
n = 3
delta = 1e-8
xValue = []
for i in range(n+1):
    xValue.append(i*d/n)

def simpsons(xValue, f):
    fx = []         #存放各节点的f(x)值
    for i in range(n+1):
        fx.append(f.evalf(subs={x: xValue[i]}))
    result = d*(fx[0]+3*fx[1]+3*fx[2]+fx[3])/8
    return result

result = simpsons(xValue, f)

Real = sp.integrate(f, (x, xValue[0], xValue[n]-delta)).evalf()    #计算真值
Et = abs(Real - result)                 #计算绝对误差
epsilon = Et / Real * 100               #计算相对误差

print("result = %.10f, Et = %.10f, epsilon = %.2f%%" % (result, Et, epsilon))
