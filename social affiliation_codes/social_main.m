
function A = social_main(N,d,c,a,ux) 
 
 initstates = zeros(N,1);  %Initialization
 initstates= false(N,1) ;
 initstates(1:N*0.01) = true ; 
 initstates = initstates(randperm(numel(initstates))); %Random distrbution
 U = sum(sum(initstates== 1));
 
 willingness=[0, 0.44, 0.28];
 
 %graph=create_graph_rnd(N,d);  
 %graph=create_graph_sf(N,d);	%One of them will be used
 graph=create_graph_sw(N,d);
 
 states = initstates;
 count = social_run(states);
 history = count;
 
 %for t= 1:200   % This runs with during given time
 while (count(1)>N*0.01) % This stops the simulation when condition provided
 
 k=(c*((count(2)/(N))^a)*ux); %Probabilty of changing affilliation
 states = social_step(states,graph,willingness,k);  %Calling the step Function
 count = social_run(states);
 history(length(history(:,1))+1,:) = count;   %Array that sums the number of agents
 
 end;
 figure(1);
 plot(history(:,2)/N)    %Plot of Fraction vs. Time
 grid on
 hold on
 
 %figure(2)
 %histfit(history(:,2))
 
