%using method two to calculate the approximation of pi, with double precision
close all;clear;clc;

n = 1;                                                      %set 'n' as the number of terms
temp1 = double_factorial(2*n-3);                            %calculate part of the item
temp2 = double_factorial(2*n-2);
item = 6 * ( temp1*0.5^(2*n-1) / (temp2*(2*n-1)) );         %calculate the first item
sum = item;                                                 %initialize 'sum'
e_a = inf;                                                  %initialize the error of current iteration results
e_s = 0.00005;                                              %set the boundary

fprintf('n=%d\tsum=%e\terror_a=%e\t\t\t\titem=%e\n', n, sum, e_a, item);

while abs(e_a) > e_s
    n = n + 1;                                              %renew the counter
    temp1 = double_factorial(2*n-3);
    temp2 = double_factorial(2*n-2);
    item = 6 * ( temp1*0.5^(2*n-1) / (temp2*(2*n-1)) );
    sum = sum + item;                                       %renew the result
    e_a = item / sum;                                       %renew the error
    
    fprintf('n=%d\tsum=%e\terror_a=%e\titem=%e\n', n, sum, e_a, item);
end


