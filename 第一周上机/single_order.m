%single precision; N = 10^2; in order
close all;clear;clc;
N = 10^2;                                       %set the limitation
n = 1 ;                                         %set 'n' as the counter
sum =  single(0);                               %initialize 'sum'
true =  single(0.5 * (1.5 - 1/N - 1/(N+1)));    %calculate the true value

while n <= N                         
    item =  single(1 / ((n+1)^2 - 1));          %calculate the item
    sum = sum + item;                           %renew the result
    n = n + 1;                                  %renew the counter
end

error =  single(abs(true - sum));               %calculate the error
fprintf('true=%e\tsum=%e\terror=%e\n', true, sum, error);


