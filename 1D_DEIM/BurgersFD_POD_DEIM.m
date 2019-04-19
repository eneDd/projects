function [solr, Vk, t_DEIM ] =  BurgersFD_POD_DEIM(k,m)
% 
% POD-DEIM reduced system and compute the solution
%
% INPUT
%
%     k = dimension of POD basis used in Galerkin projection
%     m = dimnesion of DEIM approaximation 
%
% OUTPUT
%
%    solr  = k-vec of solution of POD reduced system
%    Vk    = POD basis of dim k
%   t_DEIM = CPU time for solving the reduced system
%  
% Note: the approximate solution is Vk*solr
%

load paramBurgerFD.mat %f f0 x0 xf nu t0 tfin n dx A Ax F Anu y0 nt tspan

load BurgersSolFull.mat %tout solf

%% compute POD basis from snapshots
ns = size(solf, 2);
[V S W] = svd(solf, 'econ');
Svec = diag(S);
Vk   = V(:,1:k);

save PODbasis.mat Vk Svec


%% compute nonlinear snapshots and corr POD basis

Fss = F(solf);
[UF SF WF] = svd(Fss, 'econ');
SFvec = diag(SF);
Um   = UF(:,1:m);

save PODbasisNonlin.mat  Um SFvec 

%% plot singular values
figure(1), 
semilogy(Svec, '*'); hold on
semilogy(SFvec, 'ro');
hold off
legend('y', 'F(y)');
title(['Singular values (# snapshots=', num2str(ns), ')']);


%% DEIM pts

[p] = eimUbasis(Um,m);

save DEIMpts.mat p

%% construct POD coefficient and DEIM approx

y0_r    = Vk'*y0;
Anu_r   = Vk'*Anu*Vk;
cDEIM   = (Um(p,:)'\(Vk'*Um)')';  % I.e. cDEIM = Vk'*Um*(inv(Um(p,:)));
AxpVk   = Ax(p,:)*Vk;
Fm_deim = @(yr) -(Vk(p,:)*yr).*(AxpVk*yr);
FDEIM   = @(yr) cDEIM*Fm_deim(yr);

%% slove ODE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% solve by implicite Euler %%%%%%%%%%%%%%%%%%%

dt = (tfin - t0 )/nt;
Br = eye(k,k) -dt*Anu_r;

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
    yr = Br\(yr + dt*FDEIM(yr));
    solr(:,j+1) = yr;
    
end
t_DEIM = toc;

solDEIM0 = Vk*solr; % project back 


%% Plot

solDEIM  = [zeros(nt,1) solDEIM0' zeros(nt,1)]; % add boundaries
solDEIM  =solDEIM'; 
xx    = linspace(x0,xf,n+2);
figure(2)
surfc(xx,tspan ,solDEIM');
shading interp
title(['Sol of POD-DEIM reduced System :dim POD= ' num2str(k), ',DEIM=', num2str(m)]);
xlabel('x');
ylabel('t');
zlabel('y');
