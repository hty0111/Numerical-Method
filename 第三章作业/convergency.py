from create_matrix import *

n = 50
Yin = 0.5
A, B = create_matrix(n, Yin)

L = -np.tril(A, k=-1)
U = -np.triu(A, k=1)
D = np.triu(np.tril(A))

#Jacobi
lambda_J = max(abs(np.linalg.eigvals(np.linalg.inv(D) @ (L+U))))

#Gauss-Seidel
lambda_G = max(abs(np.linalg.eigvals(np.linalg.inv(D-L) @ U)))

print('n = %d, lambda(J) = %.6f, lambda(G) = %.6f' % (n, lambda_J, lambda_G))

