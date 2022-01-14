#method one, with double precision
import matplotlib.pyplot as plt
import numpy as np

n = 1                                       #set 'n' as the number of terms
item = (-1)**(n+1) * 4 * (1/(2*n-1))        #calculate the first item
sum = item                                  #initialize 'sum'
e_a = float('inf')                          #initialize the error of current iteration results
e_s = 0.00005                               #set the boundary

#parameters for visualization
_start = 2000
_interval = 100
x = np.array(range(_start, 12733, _interval))
y = []                                      #initialize an array to restore the value of sum

while abs(e_a) > e_s:
    n = n + 1                               #renew the counter
    item = (-1)**(n+1) * 4 * (1/(2*n-1))    #calculate the new item
    if (item > sum) and (n > 2):            #test tailing effect
        print('n=%d  sum=%e  item=%e  error_a=%e' % (n, sum, item, e_a))
    sum = sum + item                        #renew the result
    if (n % _interval == 0) and (n >= _start):
        y.append(sum)                       #add sum to the array
    e_a = item / sum                        #renew the error

print('n=%d  sum=%e  item=%e  error_a=%e' % (n, sum, item, e_a))

#visualize
plt.figure('Method One')
plt.scatter(x, y, s=1)
plt.title('starts from \'n=2000\'')
plt.xlabel('times of looping')
plt.ylabel('sum')
plt.grid()
plt.show()