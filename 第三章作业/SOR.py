from create_matrix import *

n = 20
Yin = 0.9
limit = 100                     #limitation of times of looping
tolerence = 0.0001              #terminal condition

A,B = create_matrix(n,Yin)
x = np.zeros(n)                 #initialize as '0' for first iteration

def sor(n, A, B, x, tolerence, limit, w):
    """SOR
        Arguments:
            n: dimension
            x: current solution
            tolerence: accuracy
            limit: maximum times of looping
            w: relaxation factor
    """
    times = 0

    while times < limit:
        x0 = x.copy()
        for i in range(n):
            x[i] = (1-w) * x0[i] + w * (B[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i][i]
        
        error = max(abs(x - x0))
        if error < tolerence:
            return (x, times)
        
        times += 1

    return np.ones(n), times

for i in range(10, 20):
    A,B = create_matrix(n,Yin)
    x = np.zeros(n)
    x, times = sor(n, A, B, x, tolerence, limit, i/10)
    Xout = 4 * x[0]
    Yout = x[n-1]
    print('Xout = %.6f, Yout = %.2e, w = %g, times = %d' % (Xout, Yout, i/10, times))
