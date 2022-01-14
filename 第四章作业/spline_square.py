import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = [0.0, 1.445, 2.89, 4.335, 5.78]
y = [1.8419, 2.9633, 18.236, 98.741, 529.2178]
n = 4
x_r = 3
y_r = 25

# 二次样条系数矩阵
A = np.array([[x[0], 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [x[1], 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, x[1]**2, x[1], 1, 0, 0, 0, 0, 0, 0],
              [0, 0, x[2]**2, x[2], 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, x[2]**2, x[2], 1, 0, 0, 0],
              [0, 0, 0, 0, 0, x[3]**2, x[3], 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, x[3]**2, x[3], 1],
              [0, 0, 0, 0, 0, 0, 0, 0, x[4]**2, x[4], 1],
              [1, 0, -2*x[1], -1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 2*x[2], 1, 0, -2*x[2], -1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 2*x[3], 1, 0, -2*x[3], -1, 0]])
B = np.array([y[0], y[1], y[1], y[2], y[2], y[3], y[3], y[4], 0, 0, 0])
C = (np.linalg.inv(A) @ B)

# 二次样条函数
def f(x0):
    if x[0]<= x0 <= x[1]:
        return C[0] * x0 + C[1]
    if x[1]< x0 <= x[2]:
        return C[2] * x0**2 + C[3] * x0 + C[4]
    if x[2]< x0 <= x[3]:
        return C[5] * x0**2 + C[6] * x0 + C[7]
    if x[3]< x0 <= x[4]:
        return C[8] * x0**2 + C[9] * x0 + C[10]

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
plt.title("二次样条")
plt.grid()
plt.scatter(x, y, s=20)
plt.scatter(x_r, f(x_r), s=20, label="x=3")
plt.scatter(x_ry, y_r, s=20, label="y=25")
plt.legend()
plt.show()
