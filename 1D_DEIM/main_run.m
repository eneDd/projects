function main_run
%
% To run, type: main_run
%
% Compare the solutions of the Burgers'Equation from 
% 1) Full order system 
% 2) POD reduced sytem 
% 3) POD-DEIM reduced system
%
% y(0,t) = y(1,t) =0, t \ge 0  
% y(x,0) = y_0(x),   x \in [0,1],
%
%% Solve the full-order system and collect snapshots

n = 100; % inner grid points

[solf, t_full] = BurgersFD_Full(n); 


fprintf(1,'CPU Time(sec) for solving Full system: %12.6e\n\n',t_full);


%% POD reduced system

k = 20; 

[solk, Vk, t_POD] =  BurgersFD_POD(k);
solPOD = Vk*solk;
errPOD = norm(solf-solPOD,'fro')^2; 

fprintf(1,'CPU Time(sec) for solving POD reduced system: %12.6e\n',t_POD);
fprintf(1,'Error of POD reduced order solution %12.6e\n\n',errPOD );

%% DEIM reduced system

k = 20; 
m = 20; 
 
[solk, Vk, t_DEIM ] =  BurgersFD_POD_DEIM(k,m);
solDEIM = Vk*solk;
errDEIM = norm(solf-solDEIM,'fro')^2; 

fprintf(1,'CPU Time (sec)for solving POD-DEIM reduced system: %12.6e\n',t_DEIM);
fprintf(1,'Error of POD-DEIM reduced order solution: %12.6e\n',errDEIM );
