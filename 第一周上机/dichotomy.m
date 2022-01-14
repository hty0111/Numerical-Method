%using dichotomy method to approach the zero point
close all;clear;clc;
min = 4.5;                           %initialize the value of 'min'
max = 6;                             %initialize the value of 'max'
half = 0.5 * (min + max);            %initialize the value of 'half'
temp = half;                         %restore the previous 'half' value

while f(half) ~= 0
    if f(half)*f(min) > 0            %renew the value of 'min' or 'max'
        min = half;
    else
        max = half;
    end
    half = 0.5 * (min + max);
    if abs(temp - half) < 5*10^-7    %judge the loop termination condition
        break;
    end
    temp = half;                     %renew the value of 'temp'
end

fprintf('%.6f\n', temp);