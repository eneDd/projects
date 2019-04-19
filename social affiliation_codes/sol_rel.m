function ode_rel =sol_rel(t,y) %Numerical Solution Part 1
a = 1;
c = 0.074;  %Parameters
ux = 0.65;
ode_rel(1) =(1-y(1))*c*(y(1)^a)*ux-y(1)*c*((1-y(1))^a)*(1-ux); %Equation of Model
ode_rel = [ode_rel(1)]';