%double precision; N = 10^2; in reverse order
close all;clear;clc;
N = 10^2;                                   %set the limitation
n = N ;                                     %set 'n' as the counter
sum = (0);                                  %initialize 'sum'
true = (0.5 * (1.5 - 1/N - 1/(N+1)));       %calculate the true value

while n >= 1                         
    item = (1 / ((n+1)^2 - 1));             %calculate the item
    sum = sum + item;                       %renew the result
    n = n - 1;                              %renew the counter
end

error = (abs(true - sum));                  %calculate the error
fprintf('true=%e\tsum=%e\terror=%e\n', true, sum, error);


