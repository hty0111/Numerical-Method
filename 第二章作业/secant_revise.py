from func import *

#set initial values and tolerance
delta = 0.01                #use disturbances of independent variables to estimate derivatives
x_l = 100
x_r = x_l * (1+delta)
tolerance = 1e-12
n = 0

#initialize empty lists for visualization
axis_x = []
axis_y = []

#secant method after rivision
while (abs((x_l-x_r)/x_l)>tolerance) and (n < 100):
    x_l = x_l - f(x_l) * (x_l-x_r) / (f(x_l)-f(x_r))
    x_r = x_l * (1+delta)
    
    n += 1

    axis_x.append(n)
    axis_y.append(f(x_l))

print('x = %.10f, n = %d' % (x_l, n))

#visualize
plt.figure('secant_revise')
plt.title('secant_revise')
plt.scatter(axis_x, axis_y, s=1)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()