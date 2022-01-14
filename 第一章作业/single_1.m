%using method one to calculate the approximation of pi, with single precision
close all;clear;clc;

n = 1;                                                      %set 'n' as the number of terms
item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));               %calculate the first item
sum = single (item);                                        %initialize 'sum
e_a = single (inf);                                         %initialize the error of current iteration results
e_s = single (0.00005);                                     %set the boundary

while abs(e_a) > e_s
    n = n + 1;                                              %renew the counter
    item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));           %calculate the new item
    sum = single(sum + item);                               %renew the result
    e_a = single(item / sum);                               %renew the error
end

fprintf('n=%d  sum=%e  error_a=%e\t\n', n, sum, e_a);
