import numpy as np

#input
A = np.array([[2,-1,0,0,0],\
             [-1,2,-1,0,0],\
             [0,-1,2,-1,0],\
             [0,0,-1,2,-1],\
             [0,0,0,-1,2]])
A_dimension = A.shape[0]
f = np.array([[1], [2], [3], [4], [5]], dtype=float)

#get the elements on the diagonal
a = np.diagonal(A, -1)
b = np.diagonal(A)
c = np.diagonal(A, 1)

#use fomula of Thomas algorithm to get 'beta' in matrix 'U'
beta = np.zeros(A_dimension-1)
beta[0] = c[0]/b[0]
for i in range(1, A_dimension-1):
    beta[i] = c[i]/(b[i]-a[i]*beta[i-1])

#use foward elimination to get 'y'
y = np.zeros(A_dimension)
y[0] = f[0]/b[0]
for i in range(1, A_dimension):
    y[i] = (f[i] - a[i-1]*y[i-1]) / (b[i] - a[i-1]*beta[i-1])

#use backward elimination to get 'x'
x = np.zeros(A_dimension)
x[A_dimension-1] = y[A_dimension-1]
for i in range(A_dimension-2, -1, -1):
    x[i] = y[i] - beta[i]*x[i+1]

print(x.reshape((5,1)))