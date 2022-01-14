from create_matrix import *

n = 25
Yin = 0.5
A, B = create_matrix(n, Yin)        #input

#elimination
for i in range(1,n):
    for j in range(i,n):
        factor = A[j][i-1] / A[i-1][i-1]        #elimination factor
        for k in range(i-1,n):
            A[j][k] = A[j][k] - A[i-1][k]*factor
        B[j] = B[j] - B[i-1]*factor

#back substitution
B[n-1] = B[n-1] / A[n-1][n-1]
for i in range(n-2, -1, -1):
    for j in range(n-1, i,-1):
        B[i] = B[i] - A[i][j]*B[j]
    B[i] = B[i] / A[i][i]

Xout = 4 * B[0]
Yout = B[n-1]
print('Xout = %.6f, Yout = %.2e' % (Xout, Yout))

