import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

x = [0.0, 1.445, 2.89, 4.335, 5.78]
y = [1.8419, 2.9633, 18.236, 98.741, 529.2178]
n = 4
x_r = 3
y_r = 25

# 指数拟合
lny = []
x_square = []
x_lny = []
for i in range(n + 1):
    lny.append(math.log(y[i]))
    x_square.append(x[i] ** 2)
    x_lny.append(x[i] * lny[i])

x_sum = sum(x)
lny_sum = sum(lny)
x_square_sum = sum(x_square)
x_lny_sum = sum(x_lny)

# 系数矩阵
A = np.array([[n+1, x_sum], [x_sum, x_square_sum]])
B = np.array([lny_sum, x_lny_sum])
a, b = np.linalg.inv(A) @ B

# 指数拟合函数
def f(x0):
    return math.exp(a + b*x0)

# 伪求解x的值
for i in np.arange(0, 6, 0.0001):
    if f(i) > y_r:
        x_ry = i
        break

# 计算残差、最大偏差和均方误差
offset = []
offset_square = []
for i in range(n + 1):
    offset.append(y[i] - f(x[i]))
    offset_square.append((y[i]-f(x[i])) ** 2)
offset_max = max([abs(i) for i in offset])
mse = sum(offset_square) / (1+n)

print(f(x_r))
print(x_ry)
print(offset)
print(offset_max)
print(mse)

# visualize
x_1 = []
y_1 = []
for i in np.arange(0, 6, 0.01):
    x_1.append(i)
    y_1.append(f(i))

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '12'}
matplotlib.rc('font', **font)

plt.figure("指数拟合", dpi=100)
plt.plot(x_1, y_1, linewidth='2')
plt.title("y = a * exp(bx)")
plt.grid()
plt.scatter(x, y, s=20)
plt.scatter(x_r, f(x_r), s=20, label="x=3")
plt.scatter(x_ry, y_r, s=20, label="y=25")
plt.legend()
plt.show()
