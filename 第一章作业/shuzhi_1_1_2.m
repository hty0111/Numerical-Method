%using method one to calculate the approximation of pi, with single precision
close all;clear;clc;
n = 1;
item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));     
sum = single (item);
e_a = single (inf);             
e_s = single (0.00005);            
while abs(e_a) > e_s
    n = n + 1;
    item = single ((-1)^(n+1) * 4 * (1/(2*n-1)));
    sum = single(sum + item);
    e_a = single(item / sum);
end

fprintf('n=%d\tsum=%e\terror_a=%e\t\n', n, sum, e_a);


