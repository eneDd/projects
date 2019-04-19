clear;
to = 0;
tf =1000;
yo = [0.01];
[t y] = ode45('sol_rel',[to tf],yo);  %ODE Solver

figure (1)
plot(t,y(:,1))
title('Numerical Solution with ODE Solver')
xlabel('time')
ylabel('Fraction of Non-Affiliation')
grid on

%hold on
%figure(2)
%plot(t,(1-y(:,1)))
%title('Numerical Solution with ODE Solver')
%xlabel('time')
%ylabel('Fraction of Affiliation')
%grid on