import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = [0.0, 1.445, 2.89, 4.335, 5.78]
y = [1.8419, 2.9633, 18.236, 98.741, 529.2178]
n = 4
x_r = 3
y_r = 25

# 二次函数拟合
X = np.zeros((n+1, 3))
Y = np.zeros(n+1)
# 构造范德蒙行列式并求解系数
for i in range(n + 1):
    X[i] = [1, x[i], x[i]**2]
    Y[i] = y[i]
A = X.T @ X
B = X.T @ Y
C = np.linalg.inv(A) @ B

# 拟合的二次函数
def f(x0):
    return C[0] + C[1]*x0 + C[2]*x0**2

# 伪求解x的值
for i in np.arange(0, 6, 0.0001):
    if f(i) > y_r and i > 2:
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

plt.figure("代数多项式拟合", dpi=100)
plt.plot(x_1, y_1, linewidth='2')
plt.title("y = a0 + a1*x + a2*x^2")
plt.grid()
plt.scatter(x, y, s=20)
plt.scatter(x_r, f(x_r), s=20, label="x=3")
plt.scatter(x_ry, y_r, s=20, label="y=25")
plt.legend()
plt.show()
