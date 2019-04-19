   function [p] = eimUbasis(U,m)
   %
   %    EIM interpolation indices p
   %    for the input basis U.   
   %   
   %
   %    Input:  U an n by k matrix, k .ge. m
   %
   %            m a positive integer indicating
   %              the requested number of interpolation
   %              points 
   %    
   %    Output: p an integer array of length m
   %              containing the EIM interpolation
   %              indices
   %
  
   [n,n2] = size(U);
   p = 1:n; 
   [rho,jmax] = max(abs(U(:,1)));
   p(1) = jmax;
   p(jmax) = 1; 
   for j = 2:m,
   %
   %   EIM index selection  
   %
       u = U(:,j);
       r = U(p(1:j-1),1:j-1)\u(p(1:j-1));
       u = u - U(:,1:j-1)*r;
       [rho,jmax] = max(abs(u(p(j:n)))); 
       jmax = jmax+j-1;
       itemp = p(j); p(j) = p(jmax); p(jmax) = itemp;
   end
   p = p(1:m);
