from create_matrix import *

n = 20
Yin = 0.9
A, B = create_matrix(n, Yin)        #input

#get the elements on the diagonal
a = np.diagonal(A, -1)
b = np.diagonal(A)
c = np.diagonal(A, 1)

#use formula of Thomas algorithm to get 'beta' in matrix 'U'
beta = np.zeros(n-1)
beta[0] = c[0]/b[0]
for i in range(1, n-1):
    beta[i] = c[i]/(b[i]-a[i]*beta[i-1])

#forward elimination
y = np.zeros(n)
y[0] = B[0]/b[0]
for i in range(1, n):
    y[i] = (B[i] - a[i-1]*y[i-1]) / (b[i] - a[i-1]*beta[i-1])

#backward elimination
x = np.zeros(n)
x[n-1] = y[n-1]
for i in range(n-2, -1, -1):
    x[i] = y[i] - beta[i]*x[i+1]

Xout = 4 * x[0]
Yout = x[n-1]
print('Xout = %.6f, Yout = %.2e' % (Xout, Yout))

