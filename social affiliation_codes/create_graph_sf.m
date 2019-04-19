function graph_sf = create_graph_sf(N,d)

 graph_sf = zeros(N,N);  %Initialize the main matrix
 placed = zeros(N,1);    %Initializing for subgraph
 
 for i = 1:(d+1)          %Creating the subgraph for add new vertices later  
      for j = (i+1):(d+1)
           graph_sf(i,j) = 1;
            graph_sf(j,i) = 1;
      end
       placed(i) = 1;      %Matrix of placed vertices
        end

 for i = (d+2):N 
      for l = 1:(d/2)
           prob = (graph_sf*placed).*placed.*(ones(N,1)-graph_sf(:,i)); %For adding new vertices discarding the already linked 
           prob = prob/(ones(1,N)*prob);       %Normalizing for probabilities to new links.  
           s = rand;   %Randomization
             m = 1;    %New vertices 
 while (s>prob(m))     
      s = s-prob(m);        
       m = m+1;
 end
          graph_sf(m,i) = 1;    % Adding the new vetices 
           graph_sf(i,m) = 1;    % Adding the new vetices
      end
      placed(i) = 1;  
      
 end
     r=graph_sf;                   %Adjacency Matrix
     graph_sf = sparse(graph_sf);   %Sparse Matrix 
     %draw_circ_graph(graph_sf)     % Visualization as circle
     %xlswrite('csvlist.xlsx',r)     %Exporting to Excel 
 
 
 
 