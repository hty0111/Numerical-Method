from func import *

#set initial values and tolerance
x_l = 100
x_r = 4000
tolerance = 1e-12
n = 0

#initialize empty lists for visualization
axis_x = []
axis_y = []

#bisection method
while (f(x_l)*f(x_r) != 0) and (n < 10000):
    x_mid = 0.5 * (x_l + x_r)       #iteration formula
    if abs(x_mid-x_l)/x_mid < tolerance:
        break
    
    if f(x_l)*f(x_mid) < 0:
        x_r = x_mid
    else:
        x_l = x_mid

    n += 1

    axis_x.append(n)
    axis_y.append(f(x_mid))

print('x = %.10f, n = %d' % (x_mid, n))

#visualize
plt.figure('bisection')
plt.title('bisection')
plt.scatter(axis_x, axis_y, s=3)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()
