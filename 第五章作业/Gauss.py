import sympy as sp

xValue = [0, 0.75]
def f(x0):
    return 2*sp.pi*x0*10*sp.root((1-x0/0.75), 7)

# 三阶和五阶的高斯系数表
GauThree = {0.7745966692: 0.555555556, 0: 0.8888888889}
GauFive = {0.9061798459: 0.2369268851, 0.5384693101: 0.4786286705, 0: 0.5688888889}
totalThree = 0.0
totalFive = 0.0

# 系数表代入公式
for key, value in GauThree.items():
    totalThree += f(((xValue[1]-xValue[0])*key + xValue[0] + xValue[1])/2) * value
    if key > 0:
        totalThree += f(((xValue[0]-xValue[1])*key + xValue[0] + xValue[1])/2) * value
totalThree = (totalThree*(xValue[1]-xValue[0])/2).evalf()

for key, value in GauFive.items():
    totalFive += f(((xValue[1]-xValue[0])*key + xValue[0] + xValue[1])/2) * value
    if key > 0:
        totalFive += f(((xValue[0]-xValue[1])*key + xValue[0] + xValue[1])/2) * value
totalFive = (totalFive*(xValue[1]-xValue[0])/2).evalf()

x = sp.Symbol("x")
f = 2*sp.pi*x*10*sp.root((1-x/0.75), 7)
delta = 1e-8
Real = sp.integrate(f, (x, xValue[0], xValue[1]-delta)).evalf()    #计算真值
Et3 = abs(Real - totalThree)
ep3 = Et3 / Real * 100
Et5 = abs(Real - totalFive)
ep5 = Et5 / Real * 100
print("GauThree: result = %.10f, Et = %.10f, epsilon = %.2f%%" % (totalThree, Et3, ep3))
print("GauFive: result = %.10f, Et = %.10f, epsilon = %.2f%%" % (totalFive, Et5, ep5))

