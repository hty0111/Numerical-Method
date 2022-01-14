%using method one to calculate the approximation of pi, with double precision
close all;clear;clc;
n = 1 ;                                     %set 'n' as the number of terms
item = (-1)^(n+1) * 4 * (1/(2*n-1));        %calculate the first item
sum = item;                                 %initialize 'sum'
e_a = inf;                                  %initialize the error of current iteration results
e = eps(1);                                 %set the boundary
while abs(e_a) > e
    n = n + 1;                              %renew the counter
    item = (-1)^(n+1) * 4 * (1/(2*n-1));    %calculate the new item
    sum = sum + item;                       %renew the result
    e_a = item / sum;                       %renew the error
end

fprintf('n=%d  sum=%e  error_a=%e\t\n', n, sum, e_a);

