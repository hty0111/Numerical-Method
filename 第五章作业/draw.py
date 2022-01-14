import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sp

x = np.arange(0, 0.76, 0.01)
f = 2*math.pi*x*10*(1-x/0.75)**(1/7)
plt.plot(x, f)
plt.show()
