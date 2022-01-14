from create_matrix import *

n = 20
Yin = 0.7
A, B = create_matrix(n, Yin)        #input

#Doolittle decomposition
def Doolittle(A):
    n = A.shape[0]
    L = np.zeros((n,n))
    U = np.zeros((n,n))

    U[0,:] = A[0,:]
    for i in range(n):
        L[i,i] = 1
        L[i,0] = A[i,0] / U[0,0]
    for i in range(1, n):
        for j in range(i, n):
            U[i,j] = A[i,j] - np.dot(L[i,:i], U[:i,j])
            if(j+1 < n):
                L[j+1,i] = (A[j+1,i] - np.dot(L[j+1,:i], U[:i,i])) / U[i,i]
    return L,U

L,U = Doolittle(A)

#forward elimination
y = np.zeros(n)
for i in range(n):
    y[i] = (B[i] - np.dot(L[i,:], y.T))
#backward elimination
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i,:], x.T)) / U[i,i]

Xout = 4 * x[0]
Yout = x[n-1]
print('Xout = %.6f, Yout = %.2e' % (Xout, Yout))
