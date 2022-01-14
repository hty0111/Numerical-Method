import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
delta = 1e-8
d = 0.75            #区间长度
xT = []
xS = []
eT = []
eS = []
Real = sp.integrate(f, (x, 0, 0.75-delta)).evalf()    #计算真值

def trapezoidal(n):
    xValue = []        #存放n个节点的x值
    for i in range(n + 1):
        xValue.append(i * d / n)
    fx = []             #存放各节点的f(x)值
    for i in range(n+1):
        fx.append(f.evalf(subs={x: xValue[i]}))
    result = d*(fx[0]+fx[n]+2*sum(fx[i] for i in range(1, n)))/(2*n)
    return result

def simpsons(n):
    xValue = []  # 存放n个节点的x值
    for i in range(n + 1):
        xValue.append(i * d / n)
    fx = []         #存放各节点的f(x)值
    for i in range(n + 1):
        fx.append(f.evalf(subs={x: xValue[i]}))
    total1 = 4 * sum(fx[i] for i in range(1, n, 2))
    total2 = 2 * sum(fx[i] for i in range(2, n-1, 2))
    result = d/(3*n) * (fx[0] + fx[n] + total1 + total2)
    return result

for i in range(10, 1000):
    xT.append(i)
    eT.append(Real-trapezoidal(i))
for i in range(10, 1000, 2):
    xS.append(i)
    eS.append(Real-simpsons(i))

plt.title('Contrast')
plt.plot(xT, eT, label='trapezoidal')
plt.plot(xS, eS, label='simpson')
plt.grid()
plt.legend()
plt.show()
