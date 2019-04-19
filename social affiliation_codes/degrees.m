% Compute the total degree, in-degree and out-degree of a graph based on


function [deg,indeg,outdeg]=degrees(graph)

indeg = sum(graph);
outdeg = sum(graph');

if isdirected(graph)
  deg = indeg + outdeg; % total degree

else   % undirected graph: indeg=outdeg
  deg = indeg + diag(graph)';  % add self-loops twice, if any

end