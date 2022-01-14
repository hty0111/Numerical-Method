from create_matrix import *

n = 100
Yin = 0.5
A,B = create_matrix(n, Yin)
A = A/(-17)                                             #set the maximum element as '1'
norm_A = max(np.linalg.eigvals(A @ A.T)) ** 0.5         #norm of A
A_inv = np.linalg.inv(A)
norm_A_inv = max(np.linalg.eigvals(A @ A.T)) ** 0.5     #norm of A^-1
con_num = norm_A * norm_A_inv                           #spectrum condition number
print("n = %d, Yin = %g, condition number = %.6f" % (n, Yin, con_num))


