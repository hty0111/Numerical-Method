from func import *

x_start = 500
x_end = 2000

x = list(range(x_start, x_end))
y = [f(i) for i in x]

plt.plot(x, y)
plt.grid()
plt.show()