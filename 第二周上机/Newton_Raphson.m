%Using Newton-Raphson method to find solutions to a nonlinear equation
clear;close all;clc;

x2 = pi/2-0.001;            %set the max boundary
x1 = 0.001;                 %set the min boundary
tolerance = 0.0001;         %set the tolerance to end the loop

while (abs((x2-x1)/x2)>tolerance)
x1 = x2; 
x2 = x1-f(x1)/df(x1);       %Newton formula
end

fprintf('%.8f\n', x2);

