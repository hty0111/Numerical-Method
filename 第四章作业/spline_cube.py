import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = [0.0, 1.445, 2.89, 4.335, 5.78]
y = [1.8419, 2.9633, 18.236, 98.741, 529.2178]
n = 4
x_r = 3
y_r = 25

# 三弯矩法的系数
h = np.zeros(n+1)
for i in range(1, n+1):
    h[i] = x[i] - x[i-1]
miu = np.zeros(n)
lam = np.zeros(n)
for i in range(1, n):
    miu[i] = h[i] / (h[i] + h[i+1])
    lam[i] = h[i+1] / (h[i] + h[i+1])

# 差商表
table = np.zeros((n+1, n-1))
for i in range(n + 1):
    table[i][0] = y[i]
for i in range(1, n-1):
    for j in range(i, n + 1):
        table[j][i] = (table[j][i-1] - table[j-1][i-1]) / (x[j] - x[j-i])

# 三弯矩法的系数矩阵
A = np.array([[2, lam[1], 0], [miu[2], 2, lam[2]], [0, miu[3], 2]])
g = np.zeros(n-1)
for i in range(n-1):
    g[i] = 6 * table[i+2][2]
M = np.linalg.inv(A) @ g

# 三次样条函数
def f(x0):
    if x[0]<= x0 <= x[1]:
        return M[0]*(x0-x[0])**3/(6*h[1]) + y[0]*(x[1]-x0)/h[1] + \
               (y[1]-M[0]*(h[1]**2)/6)*(x0-x[0])/h[1]
    if x[1]< x0 <= x[2]:
        return (M[1]*(x0-x[1])**3 + M[0]*(x[2]-x0)**3) / (6*h[2]) + \
               (y[1]-M[0]*h[2]**2/6)*(x[2]-x0)/h[2] + (y[2]-M[1]*(h[2]**2)/6)*(x0-x[1])/h[2]
    if x[2]< x0 <= x[3]:
        return (M[2]*(x0-x[2])**3 + M[1]*(x[3]-x0)**3)/(6*h[3]) + \
               (y[2]-M[1]*h[3]**2/6)*(x[3]-x0)/h[3] + (y[3]-M[2]*(h[3]**2)/6)*(x0-x[2])/h[3]
    if x[3]< x0 <= x[4]:
        return (M[2]*(x[4]-x0)**3)/(6*h[4]) + (y[3]-M[2]*h[4]**2/6)*(x[4]-x0)/h[4] + \
               y[4]*(x0-x[3])/h[4]

# 伪求解x的值
for i in np.arange(0, 6, 0.0001):
    if f(i) > y_r:
        x_ry = i
        break

print(f(x_r))
print(x_ry)

# visualize
x_1 = []
y_1 = []
for i in np.arange(x[0], x[4], 0.01):
    x_1.append(i)
    y_1.append(f(i))

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '12'}
matplotlib.rc('font', **font)

plt.figure("样条插值", dpi=100)
plt.plot(x_1, y_1, linewidth='2')
plt.title("三次样条")
plt.grid()
plt.scatter(x, y, s=20)
plt.scatter(x_r, f(x_r), s=20, label="x=3")
plt.scatter(x_ry, y_r, s=20, label="y=25")
plt.legend()
plt.show()
