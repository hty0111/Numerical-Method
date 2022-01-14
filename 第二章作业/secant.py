from func import *

#set initial values and tolerance
x_l = 2000
x_r = 3000
tolerance = 1e-12
n = 0

#initialize empty lists for visualization
axis_x = []
axis_y = []

#secant method
while (abs((x_l-x_r)/x_l)>tolerance) and (n < 10000):
    x_new = x_l - f(x_l) * (x_l-x_r) / (f(x_l)-f(x_r))
    if f(x_l)*f(x_r) > 0:
        if (abs(x_l)-abs(x_new)) < (abs(x_r)-abs(x_new)):
            x_r = x_new
        else:
            x_l = x_new
    else:
        if f(x_new)*f(x_l) > 0:
            x_r = x_new
        else:
            x_l = x_new
    
    n += 1

    axis_x.append(n)
    axis_y.append(f(x_new))

print('x = %.10f, n = %d' % (x_new, n))

#visualize
plt.figure('secant')
plt.title('secant')
plt.scatter(axis_x, axis_y, s=1)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()