from func import *

#set initial values and tolerance
x_l = 100
x_r = 4000
tolerance = 1e-12
n = 0
flag1 = flag2 = 0             #use flags to see whether one of the boundary is fixed 

#initialize empty lists for visualization
axis_x = []
axis_y = []

#find out a new 'x', where its function value is half of the param's 
def half(x):
    if f(x) > 0:
        for i in range(int(x), 10000):
            if f(i) < 0.5*f(x):
                return i
    else:
        for i in range(int(x), 0):
            if f(i) > 0.5*f(x):
                return i

#false-position method after revision
while (f(x_l)*f(x_r) != 0) and (n < 10000):
    x_new = x_r - f(x_r) * (x_l-x_r) / (f(x_l) - f(x_r))    #iteration formula
    if f(x_r)*f(x_new) > 0:
        x_r = x_new
        if flag1 == 0:      #see whether the boundary is fixed or not
            flag1 = 1
            flag2 = 0
        else:
            x_l = half(x_l)
        if abs(x_l-x_new)/x_new < tolerance:
            break
    else:
        x_l = x_new
        if flag2 == 0:
            flag2 = 1
            flag1 = 0
        else:
            x_r = half(x_r)       
        if abs(x_r-x_new)/x_new < tolerance:
            break

    n += 1

    axis_x.append(n)
    axis_y.append(f(x_new))

print('x = %.10f, n = %d' % (x_new, n))
    
#visualize
plt.figure('false_position_revise')
plt.title('false_position_revise')
plt.scatter(axis_x, axis_y, s=5)
plt.xlabel('times of looping')
plt.ylabel('value of f(x)')
plt.grid()
plt.show()