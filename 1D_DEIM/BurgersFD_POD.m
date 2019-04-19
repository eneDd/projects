function [solr, Vk, t_POD]= BurgersFD_POD(k)
% 
% Construct a POD reduced system and compute the solution
%
% INPUT
%     k = dimension of POD reduced sytem
%
% OUTPUT
%
%    solr = k-vec of solution of POD reduced system
%    Vk   = POD basis of dim k
%  t_POD  = CPU time for solving the reduced system
%  
% Note: the approximate solution is Vk*solr
%
load paramBurgerFD.mat %f f0 x0 xf nu t0 tfin n dx A Ax F Anu y0 nt tspan

load BurgersSolFull.mat %tout solf

%% select snapshots for computing POD basis

SS = solf;
ns = size(SS,2);
%% compute POD basis from snapshots
[V S W] = svd(solf, 'econ');
Svec = diag(S);
Vk   = V(:,1:k);

save PODbasis.mat Vk Svec

%% plot singular values
figure, 
semilogy(Svec, '*');
title(['Singular values (# snapshots=', num2str(ns), ')']);


%% construct POD coefficient

Anu_r = Vk'*Anu*Vk;
y0_r  = Vk'*y0;

%% slove ODE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% semi-implicite Euler %%%%%%%%%%%%%%%%%%%

dt = (tfin - t0 )/nt;
Bk = eye(k,k) -dt*Anu_r; 

tout = zeros(nt,1);
tout(1) = t0; 
t = t0;

solr = zeros(k,nt);
solr(:,1) = y0_r; 
yr = y0_r;

tic
for j = 1:nt-1,
     t=  t + dt; 
    tout(j+1) = t;  
      
    yr = Bk\(yr + dt*Vk'*F(Vk*yr));
    solr(:,j+1) = yr;
end
t_POD = toc;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

solPOD0 = Vk*solr; % project back 


%% Plot

solPOD  = [zeros(nt,1) solPOD0' zeros(nt,1)]; % add boundaries
solPOD  =solPOD'; 
xx      = linspace(x0,xf,n+2);

figure
surfc(xx,tspan ,solPOD');
shading interp
title(['Sol of POD reduced System :dim POD= ' num2str(k)]);
xlabel('x');
ylabel('t');
zlabel('y');


