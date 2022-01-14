%Using secant method to find solutions to a nonlinear equation
clear;close all;clc

x1 = pi/2-0.001;            %set the max boundary
x2 = 0;                     %set the min boundary
tolerance = 0.0001;         %set the tolerance to end the loop

while (abs((x2-x1)/x2)>tolerance)
    x3 = x2 - f(x2) * (x2-x1) / (f(x2)-f(x1));      %new value of 'x'
    
    %renew 'x1'&'x2'
    if f(x2)*f(x1) > 0                              
        if (abs(x2)-abs(x3)) < (abs(x1)-abs(x3))  x1 = x3;   
        else  x2 = x3;
        end
    else
        if f(x3)*f(x2) > 0  x1 = x3;
        else  x2 = x3;
        end
    end
end
fprintf('%.8f\n', x3);
