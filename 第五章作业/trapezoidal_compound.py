import sympy as sp

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
d = 0.75                #区间长度
n = 10                  #分段数
delta = 1e-8            #微小偏移量
xValue1 = []            #存放n个节点的x值
for i in range(n + 1):
    xValue1.append(i * d / n)
xValue2 = []            #存放n/2个节点的x值
for i in range(int(n/2 + 1)):
    xValue2.append(i * 2*d / n)

def trapezoidal(xValue, n0):
    fx = []             #存放各节点的f(x)值
    for i in range(n0+1):
        fx.append(f.evalf(subs={x: xValue[i]}))
    result = d*(fx[0]+fx[n0]+2*sum(fx[i] for i in range(1, n0)))/(2*n0)
    return result

result = trapezoidal(xValue1, n)

Ea = (trapezoidal(xValue1, n)-trapezoidal(xValue2, int(n/2))) / 3    #计算事后误差
Real = sp.integrate(f, (x, xValue1[0], xValue1[n]-delta)).evalf()    #计算真值
Et = abs(Real - result)                 #计算绝对误差
epsilon = Et / Real * 100               #计算相对误差

print("result = %.10f, Et = %.10f, epsilon = %.2f%%, Ea = %.10f" %
      (result, Et, epsilon, Ea))

