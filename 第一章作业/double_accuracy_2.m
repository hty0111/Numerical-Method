%using method two to calculate the approximation of pi, with double precision
close all;clear;clc;

n = 1;
temp1 = double_factorial(2*n-3);
temp2 = double_factorial(2*n-2);
item = 6 * ( temp1*0.5^(2*n-1) / (temp2*(2*n-1)) );
sum = item;
e_a = inf;        
e = eps(1);                                         %change the boundary

while abs(e_a) > e
    n = n + 1;
    temp1 = double_factorial(2*n-3);
    temp2 = double_factorial(2*n-2);
    item = 6 * ( temp1*0.5^(2*n-1) / (temp2*(2*n-1)) );
    sum = sum + item;
    e_a = item / sum;
end

fprintf('n=%d\tsum=%e\terror_a=%e\n', n, sum, e_a);

