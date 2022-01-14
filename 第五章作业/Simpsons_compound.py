import sympy as sp

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
d = 0.75            #区间长度
n = 10              #分段数
delta = 1e-10       #由于计算机内部存储格式的原因，用库函数计算真值时需要将积分边界减去微小量
xValue1 = []        #存放n个节点的x值
for i in range(n + 1):
    xValue1.append(i * d / n)
xValue2 = []        #存放n/2个节点的x值
for i in range(int(n/2 + 1)):
    xValue2.append(i * 2*d / n)

def simpsons(xValue, n0):
    fx = []         #存放各节点的f(x)值
    for i in range(n0+1):
        fx.append(f.evalf(subs={x: xValue[i]}))
    total1 = 4 * sum(fx[i] for i in range(1, n0, 2))
    total2 = 2 * sum(fx[i] for i in range(2, n0-1, 2))
    result = d/(3*n0) * (fx[0] + fx[n0] + total1 + total2)
    return result

result = simpsons(xValue1, n)
Real = sp.integrate(f, (x, xValue1[0], xValue1[n]-delta)).evalf()    #计算真值
Et = abs(Real - result)                         #计算绝对误差
epsilon = Et / Real * 100                       #计算相对误差
Ea = (simpsons(xValue1, n)-simpsons(xValue2, int(n/2))) / 15      #计算事后误差

print("result = %.10f, Et = %.10f, epsilon = %.2f%%, Ea = %.10f" % (result, Et, epsilon, Ea))
