close all; clear; clc;
fprintf('输入系数矩阵：')
a=input('Coefficient_matrix_a=');      
fprintf('输入增广矩阵的最后一列：')
b=input('matrix_b=');         	
n=length(b);

%deal with input
for i = 1 : n-1
    for k = i+1 : n
    l(k,i) = -a(k,i) / a(i,i);
    for j = i : n
        a(k,j) = a(k,j) + l(k,i) * a(i,j);
    end
    b(k) = b(k) + l(k,i) * b(i);
    end
end

Augmented_matrix = [a,b];       %augmented matrix
x(n)=b(n)/a(n,n);

%Gauss elimination method
for i = n-1:-1:1
    k=0;
    for j = i+1 : n
        k = k + a(i,j)*x(j);
    end
    x(i) = (b(i)-k) / a(i,i);
end

x=x'