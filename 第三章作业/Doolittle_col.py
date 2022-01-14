from create_matrix import *

n = 20
Yin = 0.9
A, B = create_matrix(n, Yin)        #input

def Doolittle_Col(matrix):
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    U[0,:] = matrix[0,:]
    for i in range(n):
        L[i,i] = 1
        L[i,0] = matrix[i,0] / U[0,0]
    
    #column pivot
    for i in range(1, n):
        max_index = i               #store the index of the largest value in column
        max_value = float('-inf')   #initialize the max value
        
        for k in range(i, n):
            temp_value = matrix[k,i] - np.dot(L[k,:i], U[:i,i])
            if(max_value < temp_value):
                max_index = k
                max_value = temp_value
        matrix[[i,max_index],:] = matrix[[max_index,i],:]   #exchange
        L[[i,max_index],:i] = L[[max_index,i],:i]           #exchange
        
        for j in range(i, n):
            U[i,j] = matrix[i,j] - np.dot(L[i,:i], U[:i,j])
            if(j+1 < n):
                L[j+1,i] = (matrix[j+1,i] - np.dot(L[j+1,:i], U[:i,i])) / U[i,i]
    
    return L,U
    
L,U = Doolittle_Col(A)

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
