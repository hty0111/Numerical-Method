from func import *

#define the simplest 'g(x)'
def g(x):
    return x + f(x)
    
#find out the initial value for iteration
for i in range(100, 10000, 100):
    if (df(i) + 1) > -0.5:
        x_1 = i
        break

#set initial values and tolerance
tolerance = 1e-12
n = 0

#initialize empty lists for visualization
axis_x = []
axis_y = []

#fixed-point method
while n < 10000:
    x_2 = g(x_1)
    if abs(x_2-x_1)/x_2 < tolerance:
        break
    x_1 = x_2

    n += 1

    axis_x.append(n)
    axis_y.append(f(x_2))

print('x = %.10f, n = %d' % (x_2, n))

#visualize 
plt.figure('fixed_point')
plt.title('fixed_point')
plt.scatter(axis_x, axis_y, s=1)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()


    