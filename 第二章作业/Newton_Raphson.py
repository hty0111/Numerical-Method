from func import *

#set initial values and tolerance
x_1 = 100
n = 0
tolerance = 1e-12

#initialize empty lists for visualization
axis_x = []
axis_y = []

#Newton-Raphson method
while n < 10000:
    x_2 = x_1 - f(x_1) / df(x_1)
    if abs(x_2-x_1)/x_2 < tolerance:
        break
    x_1 = x_2

    n += 1

    axis_x.append(n)
    axis_y.append(f(x_2))

print('x = %.10f, n = %d' % (x_2, n))

#visualize
plt.figure('Newton_Raphson')
plt.title('Newton_Raphson')
plt.scatter(axis_x, axis_y, s=5)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()