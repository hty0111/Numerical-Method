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

table_1 = np.zeros((n_1+1, n_1+1))
table_2 = np.zeros((n_2+1, n_2+1))

# 创建差商表
for i in range(n_1+1):
    table_1[i][0] = y_1[i]
for i in range(1, n_1+1):
    for j in range(i, n_1+1):
        table_1[j][i] = (table_1[j][i-1] - table_1[j-1][i-1]) / (x_1[j] - x_1[j-i])

for i in range(n_2+1):
    table_2[i][0] = y_2[i]
for i in range(1, n_2+1):
    for j in range(i, n_2+1):
        table_2[j][i] = (table_2[j][i-1] - table_2[j-1][i-1]) / (x_2[j] - x_2[j-i])

# 提取牛顿插值多项式的系数
a_1 = np.diagonal(table_1)
a_2 = np.diagonal(table_2)

# 牛顿插值公式
def newton(x, x_temp, n, a):
    total = a[0]
    for k in range(1, n+1):
        product = 1
        for j in range(0, k):
            product *= x - x_temp[j]
        total += a[k] * product
    return total

# 伪求解x的值
for i in np.arange(0, 6, 0.0001):
    if newton(i, x_1, n_1, a_1) > y_r:
        x_ry1 = i
        break
for i in np.arange(0, 6, 0.0001):
    if newton(i, x_2, n_2, a_2) > y_r and i > 3:
        x_ry2 = i
        break

print(newton(x_r, x_1, n_1, a_1))
print(newton(x_r, x_2, n_2, a_2))
print(x_ry1)
print(x_ry2)

# visualize
x = []
y1 = []
y2 = []
for i in np.arange(0, 6, 0.01):
    x.append(i)
    y1.append(newton(i, x_1, n_1, a_1))
for i in np.arange(0, 6, 0.01):
    y2.append(newton(i, x_2, n_2, a_2))

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '12'}
matplotlib.rc('font', **font)

plt.figure('Newton', dpi=100)
plt.title("Newton")
plt.plot(x, y1, label='四次插值', linewidth='0.5')
plt.plot(x, y2, label='二次插值', linewidth='0.5')
plt.scatter(x_r, newton(x_r, x_1, n_1, a_1), s=8, label="四次插值，x=3")
plt.scatter(x_r, newton(x_r, x_2, n_2, a_2), s=8, label="二次插值，x=3")
plt.scatter(x_ry1, y_r, s=8, label="四次插值，y=25")
plt.scatter(x_ry2, y_r, s=8, label="二次插值，y=25")
plt.grid()
plt.legend()
plt.show()
