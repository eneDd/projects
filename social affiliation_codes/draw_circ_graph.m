% Draw a circular graph with links and nodes in order of degree

function [] = draw_circ_graph(graph)

n = size(graph,1); % number of nodes
[degs,~,~]=degrees(graph);
[~, Y] = sort(degs);   % Y - sorted nodal indices
angl = 2*pi/n; % rotation angle

for k=1:n
  x(Y(k)) = real(exp(angl*(k-1)*i));
  y(Y(k)) = imag(exp(angl*(k-1)*i));
end

for k=1:n
  plot(x(k),y(k),'ko')
  text(1.1*x(k),1.1*y(k),strcat('v',num2str(k)));
  hold off; hold on;
end

edges=find(graph>0);
set(gcf,'Color',[1,1,1])

for e=1:length(edges)
    [ii,jj]=ind2sub([n,n],edges(e));
    line([x(ii) x(jj)],[y(ii) y(jj)],'Color','k');
    hold off; hold on;
end
axis off;