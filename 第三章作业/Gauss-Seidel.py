from create_matrix import *

n = 20
Yin = 0.9
limit = 100                     #limitation of times of looping
tolerence = 0.0001              #terminal condition

A,B = create_matrix(n,Yin)
x = np.zeros(n)                 #initialize as '0' for first iteration

def gauss_seidel(n, A, B, x, tolerence, limit):
    """Gauss–Seidel
        Arguments:
            n: dimension
            x: current solution
            tolerence: accuracy
            limit: maximum times of looping
    """
    times = 0

    while times < limit:
        x0 = x.copy()
        for i in range(n):
            x[i] = (B[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i][i]
        
        error = max(abs(x - x0))
        if error < tolerence:
            return (x, times)
        
        times += 1
    
    return np.ones(n), times
        
x, times = gauss_seidel(n, A, B, x, tolerence, limit)
Xout = 4 * x[0]
Yout = x[n-1]
print('Xout = %.6f, Yout = %.2e, times = %d' % (Xout, Yout, times))
