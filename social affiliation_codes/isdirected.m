% Using the matrix transpose function

function S=isdirected(graph)

S = true;
if graph==transpose(graph); S = false; end

% one-liner alternative: S=not(issymmetric(adj));