from func import *

#set initial values and tolerance
x_l = 100
x_r = 4000
tolerance = 1e-12
n = 0

#initialize empty lists for visualization
axis_x = []
axis_y = []

#false-position method
while (f(x_l)*f(x_r) != 0) and (n < 10000):
    x_new = x_r - f(x_r) * (x_l-x_r) / (f(x_l) - f(x_r))
    if f(x_r)*f(x_new) > 0:
        x_r = x_new
        if abs(x_l-x_new)/x_new < tolerance:
            break
    else:
        x_l = x_new
        if abs(x_r-x_new)/x_new < tolerance:
            break

    n += 1

    axis_x.append(n)
    axis_y.append(f(x_new))

print('x = %.10f, n = %d' % (x_new, n))

#visualize    
plt.figure('false_position')
plt.title('false_position')
plt.scatter(axis_x, axis_y, s=1)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()

