import matplotlib.pyplot as plt
import numpy as np

n = 12

def f(x_1):
    return 1 / ((x_1-0.3)**2 + 0.01) + 1 / ((x_1-0.9)**2 + 0.04) - 6

#draw the original figure
interval = 0.01
x_0 = np.arange(0, 1 + interval, interval)
y_0 = []
for i in x_0:
    y_0.append(f(i))

#Newton
table = np.zeros((n+1, n+1))
x_1 = np.arange(0, 1 + 1/n, 1/n)

#create difference quotient table
y = []
for i in x_1:
    y.append(f(i))

for i in range(n+1):
    table[i][0] = y[i]
for i in range(1, n+1):
    for j in range(i, n+1):
        table[j][i] = (table[j][i-1] - table[j-1][i-1]) / (x_1[j] - x_1[j-i])

#store coefficients
a = np.diagonal(table)

#define Newton interpolation polynomial 
def Newton(x, x_1, n, a):
    sum = a[0]
    for i in range(1, n+1):
        product = 1
        for j in range(0, i):
            product *= x - x_1[j]
        sum += a[i] * product
    return sum

y_1 = []
for i in x_0:
    y_1.append(Newton(i, x_1, n, a))

#piecewise linear interpolation
y_2 = []
for i in x_1:
    y_2.append(f(i))

#visualize
plt.figure('Contrast')
plt.plot(x_0, y_0, label='Original Figure', linewidth='0.5')
plt.plot(x_0, y_1, label='Newton Interpolation', linewidth='0.5')
plt.plot(x_1, y_2, label='Linear Interpolation', linewidth='0.5')
plt.xticks(x_0[::10])
plt.title('n = {}'.format(n))
plt.grid()
plt.legend()
plt.show()
