 function graph_rnd = create_graph_rnd(N,d)
 
graph_rnd = zeros(N,N); % Initialize 

for i = 1:(d*N/2) % Number of Vertices 
 j = floor(N*rand)+1;  %Random 
 k = floor(N*rand)+1;  %Random
 while (j==k)||(graph_rnd(j,k)==1) % If the same pair is chosen, tries again
 j = floor(N*rand)+1;
 k = floor(N*rand)+1;
 end;
 graph_rnd(j,k)=1;   %Sending to adjanceny matrix 
 graph_rnd(k,j)=1;   %Sending to adjanceny matrix 
 end;
 r=graph_rnd;
 graph_rnd = sparse(graph_rnd); %Stored As Sparse Matrix 
 
 %draw_circ_graph(graph_rnd) %Calls for the drawing function
 %xlswrite('csvlist.xlsx',r) %Writes as .csv file
 
 
 end
 
 