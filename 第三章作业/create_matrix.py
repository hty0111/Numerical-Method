import numpy as np

def create_matrix(n, Yin):
    A = np.zeros(n)                 #initialize
    A[0] = 17
    A[1] = -12

    #add by line
    for i in range(1, n):
        temp = np.zeros(n)         
        if i == n-1:
            temp[n-2] = -5
            temp[n-1] = 17
        else:
            temp[i-1] = -5
            temp[i] = 17
            temp[i+1] = -12
        A = np.vstack((A, temp))    #vertical splicing 
    B = np.zeros(n)
    B[0] = 5 * Yin

    return A, B

        