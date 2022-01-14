%using method one to calculate the approximation of pi, with single precision
close all;clear;clc;
n = 1;
item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));     
sum = single (item);
e_a = single (inf); 
e = eps(single(1));                             %change the boundary
while abs(e_a) > e
    n = n + 1;
    item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));
    sum = single(sum + item);
    e_a = single(item / sum);
end

fprintf('n=%d  sum=%e  error_a=%e\t\n', n, sum, e_a);


