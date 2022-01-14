import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x_1 = [0.0, 1.445, 2.89, 4.335, 5.78]
y_1 = [1.8419, 2.9633, 18.236, 98.741, 529.2178]
n_1 = 4     #四次插值

x_2 = [1.445, 2.89, 4.335]
y_2 = [2.9633, 18.236, 98.741]
n_2 = 2     #二次插值

x_r = 3
y_r = 25

# 求拉格朗日插值多项式的系数
def l_1(i, x):
    mul = 1
    for j in range(n_1 + 1):
        if j != i:
            mul *= (x-x_1[j]) / (x_1[i]-x_1[j])
    return mul

def l_2(i, x):
    mul = 1
    for j in range(n_2 + 1):
        if j != i:
            mul *= (x-x_2[j]) / (x_2[i]-x_2[j])
    return mul

# 拉格朗日插值公式
def f_1(x0):
    return y_1[0]*l_1(0, x0) + y_1[1]*l_1(1, x0) + y_1[2]*l_1(2, x0) + \
           y_1[3]*l_1(3, x0) + y_1[4]*l_1(4, x0)

def f_2(x0):
    return y_2[0]*l_2(0, x0) + y_2[1]*l_2(1, x0) + y_2[2]*l_2(2, x0)

# 伪求解x的值
for i in np.arange(0, 6, 0.0001):
    if f_1(i) > y_r:
        x_ry1 = i
        break
for i in np.arange(0, 6, 0.0001):
    if f_2(i) > y_r and i > 3:
        x_ry2 = i
        break

print(f_1(x_r))
print(f_2(x_r))
print(x_ry1)
print(x_ry2)

# visualize
x = []
y1 = []
y2 = []
for i in np.arange(0, 6, 0.01):
    x.append(i)
    y1.append(f_1(i))
for i in np.arange(0, 6, 0.01):
    y2.append(f_2(i))

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '12'}
matplotlib.rc('font', **font)

plt.figure("Lagrange", dpi=100)
plt.plot(x, y1, label="四次插值", linewidth='0.5')
plt.plot(x, y2, label="二次插值", linewidth='0.5')
plt.title("Lagrange")
plt.scatter(x_r, f_1(x_r), s=8, label="四次插值，x=3")
plt.scatter(x_r, f_2(x_r), s=8, label="二次插值，x=3")
plt.scatter(x_ry1, y_r, s=8, label="四次插值，y=25")
plt.scatter(x_ry2, y_r, s=8, label="二次插值，y=25")
plt.legend()
plt.grid()
plt.show()
