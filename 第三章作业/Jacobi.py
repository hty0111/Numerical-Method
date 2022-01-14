from create_matrix import *

n = 20
Yin = 0.9
limit = 100                     #limitation of times of looping
tolerence = 0.0001              #terminal condition

A,B = create_matrix(n,Yin)
x0 = np.zeros(n)                #initialize as '1' for first iteration
x = np.zeros(n)                 #initialize as '0' for first iteration

def jacobi(n, A, B, x0, x, tolerence, limit):
    """Jacobi
        Arguments:
            n: dimension
            x: current solution
            x0: previous solution
            tolerence: accuracy
            limit: maximum times of looping
    """
    times = 0

    while times < limit:
        for i in range(n):
            temp = 0
            for j in range(n):
                if i != j:
                    temp += x0[j] * A[i][j]
            x[i] = ((B[i] - temp) / A[i][i])
        error = max(abs(x - x0))
        
        if error < tolerence:
            return (x, times)
        else:
            x0 = x.copy()
        
        times += 1
    
    return np.ones(n), times

x, times = jacobi(n, A, B, x0, x, tolerence, limit)
Xout = 4 * x[0]
Yout = x[n-1]
print('Xout = %.6f, Yout = %.2e, times = %d' % (Xout, Yout, times))