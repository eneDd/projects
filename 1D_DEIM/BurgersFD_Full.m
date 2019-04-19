function [solf, t_full] = BurgersFD_Full(n)
%
% 1) Set up parameters for 1D Burgers'Equation
%
% 2) Solve using finite difference
%
% INPUT 
%
%    n =  inner grid points (not include the boundary points)
%
% OUTPUT
%
%   solf   = n-by-nt matrix of the solution at tj, j = 1,..., nt
%   t_full = CPU time for solving full-order system
%

f = inline('exp(-(15.*(x-.5)).^2)','x');
f0 = @(x) f(x)-f(0);

x0 = 0; 
xf = 1;
nu = 0.1;
t0 = 0;
tfin = 1;

%coeff matrices from FD  discretization

dx = (xf- x0)/(n+1);
d1 = repmat(1/(2*dx),n,1);
d2 = repmat(1/(dx^2),n,1);
A = spdiags([d2 -2*d2  d2], -1:1, n, n); 
Ax = spdiags([-d1 0*d1  d1], -1:1, n, n); 
F = @(y) -y.*(Ax*y);
Anu =nu*A;

% param for solving ODEs

xs  = linspace(x0, xf, n+2)';
y0 = f0(xs(2:n+1));

nt     = 100;
tspan  = linspace(t0,tfin,nt);

save paramBurgerFD.mat f f0 x0 xf nu t0 tfin n dx A Ax F Anu y0 nt tspan

%% Solve using FD 
%%%%%%% solve by semi-implicite Euler %%%%%%%%%%%%%%%%%%%

dt = (tfin - t0 )/nt;

B = eye(n,n)-dt*Anu;
tout = zeros(nt,1);
tout(1) = t0; 
t = t0;

solf = zeros(n,nt);
solf(:,1) = y0; 
y = y0;

tic
for j = 1:nt-1,
    
    t=  t + dt; 
    tout(j+1) = t;  
    y = B\(y + dt*F(y)) ;  
    solf(:,j+1) = y;
    
end
t_full = toc; 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
save BurgersSolFull.mat tout solf


%% Plot
solf1  = [zeros(nt,1) solf' zeros(nt,1)]; % add boundaries
xx    = linspace(x0,xf,n+2);

figure
surfc(xx,tspan ,solf1);
shading interp
title(['Sol of Full System (FD):dim = ' num2str(n)]);
xlabel('x');
ylabel('t');
zlabel('y');
%axis([x0,xf,t0,tf,zmin,zmax]);


