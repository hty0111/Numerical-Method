import numpy as np

#input
A = np.array([[2,-1,0,0,0],\
             [-1,2,-1,0,0],\
             [0,-1,2,-1,0],\
             [0,0,-1,2,-1],\
             [0,0,0,-1,2]])
f = np.array([[1], [2], [3], [4], [5]], dtype=float)

#revise the method of Cholesky decomposition by avoiding square root
def Cholesky_revise(matrix):
    dimension = matrix.shape[0]
    L = np.zeros((dimension, dimension))
    for i in range(dimension):
        L[i,i] = 1
    D = np.zeros((dimension, dimension))
    for i in range(dimension):
        D[i,i] = matrix[i,i] - np.dot(np.dot(L[i,:i],D[:i,:i]), L[i,:i].T)
        for j in range(i+1, dimension):
            L[j,i] = (matrix[j,i] - np.dot(np.dot(L[j,:i],D[:i,:i]), L[i,:i].T)) / D[i,i]
    return L, D

L, D = Cholesky_revise(A)

y = np.linalg.inv(L) @ f        # Y = L^-1 * B

x = np.linalg.inv(D @ L.T) @ y  # X = (D*L.T)^-1 * Y

print(x)

