 function graph_sw = create_graph_sw(N,d)
 
prompt = 'Probability value? ';
p = input(prompt)
 
 graph_sw = sparse(zeros(N,N));  %Initialization
 N_initial_edge=floor(floor(d+.5)/2);
 
 for i = 1:N                    %Creating first random graph
 for link = 1:N_initial_edge
 graph_sw(i,mod(i+link-1,N)+1)=1;
 end;
 end;
 k=floor(d+.5)/2;
 if(floor(k)<k)
 for i =1:2:N
 graph_sw(i,mod(i+floor(k),N)+1)=1;
 end;
 end;
 for i=1:N
 for j=i+1:N
 if(graph_sw(i,j)==1 && rand()<p)
 graph_sw(i,j)=0;
 a=floor(rand()*N)+1;
 while(graph_sw(a,i)==1 || graph_sw(i,a)==1 || i==a)
 a=floor(rand()*N)+1;
 end;
 if(i<a)
 graph_sw(i,a)=1;
 else
 graph_sw(a,i)=1;
 end;
 end;
 end;
 end;
 
 if d<floor(d+.5)           %Deleting the edges and rewiring with the value of "p"
 N_edge_removed=0;
 N_edge_to_remove=floor((floor(d+.5)-d)*N);
 while(N_edge_to_remove>N_edge_removed)
 for i=1:N
 for j=i+1:N
 if(N_edge_to_remove>N_edge_removed && graph_sw(i,j)==1 && rand()<N_edge_to_remove/(N_edge_per_vertice*N))
 graph_sw(i,j)=0;
 N_edge_removed=N_edge_removed+2;
 end;
 end;
 end;
 end;
 else
 N_edge_added=0;
 N_edge_to_add=floor((d-floor(d+.5))*N);
 while(N_edge_to_add>N_edge_added)
 for i=1:N
 for j=i+1:N
 if(N_edge_to_add>N_edge_added && graph_sw(i,j)==0 && rand()<N_edge_to_add/(N_edge_per_vertice*N))
 graph_sw(i,j)=1;
 N_edge_added=N_edge_added+2;
 end;
 end;
 end;
 end;
 end;
 graph_sw = graph_sw+graph_sw';
 r=full(graph_sw);
 
 draw_circ_graph(graph_sw)      % Draws a circulation picture for graph
 xlswrite('csvlist.xlsx',r)     %Writes the Sparse Matrix
 
 
 