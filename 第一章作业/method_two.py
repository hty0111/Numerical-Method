#method two, with double precision
import matplotlib.pyplot as plt
import numpy as np

def dbl_fact(x):                    #define a function to calculate double factorial
    if x == 0 or x == -1:
        return 1
    else:
        return x * dbl_fact(x-2)

#parameters for visualization
_start = 4
x = np.array(range(_start, 24))
y = []                              #initialize an array to restore the value of sum

n = 1                                    
temp_1 = dbl_fact(2*n-3)            
temp_2 = dbl_fact(2*n-2)
item = 6 * (temp_1 * 0.5**(2*n-1) / (temp_2 * (2*n-1)))
sum = item                          #initialize 'sum'
e_a = float('inf')                  #initialize the error of current iteration results
e_s = 0.00005                       #set the boundary

e = 1                               #calculate the machine accuracy
while 1+e > 1:
    e /= 2
e *= 2

#while abs(e_a) > e_s:
while abs(e_a) > e:
    n = n + 1                             #renew the counter
    temp_1 = dbl_fact(2*n-3)            
    temp_2 = dbl_fact(2*n-2)
    item = 6 * (temp_1 * 0.5**(2*n-1) / (temp_2 * (2*n-1)))
    sum = sum + item                      #renew the result
    if n >= _start:
        y.append(sum)
    e_a = item / sum                      #renew the error

print('n=%d  sum=%e  item=%e  error_a=%e' % (n, sum, item, e_a))

#visualize
plt.figure('Method Two')
plt.scatter(x, y, s=25)
plt.title('starts from 4')
plt.xlabel('times of looping')
plt.ylabel('sum')
plt.grid()
plt.show()