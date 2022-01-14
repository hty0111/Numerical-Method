import numpy as np

#input
A = np.array([[2,-1,0,0,0],\
             [-1,2,-1,0,0],\
             [0,-1,2,-1,0],\
             [0,0,-1,2,-1],\
             [0,0,0,-1,2]])
A_dimension = A.shape[0]
f = np.array([[1], [2], [3], [4], [5]], dtype=float)

#find a matrix to meet the Cholesky decomposition
def Cholesky(matrix):
    dimension = matrix.shape[0]                 #calculate the dimension of A
    C = np.zeros((dimension, dimension))        #initialize a new matrix
    
    #use fomula of Cholesky decomposition
    for i in range(dimension):
        C[i,i] = (matrix[i,i] - np.dot(C[i,:i],C[i,:i].T))**0.5
        for j in range(i+1, dimension):
            C[j,i] = (matrix[j,i] - np.dot(C[j,:i],C[i,:i].T)) / C[i,i]
    return C

L = Cholesky(A)

#use foward elimination to get 'y'
y = np.zeros(A_dimension)
y[0] = f[0]/L[0][0]
for i in range(1, A_dimension):
    sum = 0
    for j in range(i):
        sum += L[i][j]*y[j]
    y[i] = (f[i]-sum) / L[i][i]

#use backward elimination to get 'x'
x = np.zeros(A_dimension)
x[4] = y[4]/L[4][4]
for i in range(A_dimension-2, -1, -1):
    sum = 0
    for j in range(A_dimension-1, i, -1):
        sum += L[j][i] * x[j]
    x[i] = (y[i]-sum) / L[i][i]

print(list(x))

