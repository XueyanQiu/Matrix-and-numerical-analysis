A = [2,-1.0,0;
     -1.0,2,-1;
     0,-1,2.0];
N=100;
ep=1e-3;
n=length(A);
y=ones(n,1);
k=0;
m1=0;
while k<=N
   x=A*y;
   m=max(abs(x));
   disp(m);
   y=x/m
   if abs(m-m1)<ep
        break;
   end          
   m1=m;
   k=k+1;
end

final_answer_u = m;
final_answer_x = x;