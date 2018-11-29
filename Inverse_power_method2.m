A = [3,0,-10;
     -1,3,4;
     0,1,-2];
p=4.3;%原点位移
I=[1,0,0;
    0,1,0;
    0,0,1];
N=1000;
ep=1e-5;
n=length(A);
u=ones(n,1);
times =0;
m1=0;
while times<N
    v=inv(A-p*I)*u;
    times=times+1;
    m=max(abs(v));
    u=v/m;
    disp(times);
    disp(v);
    disp(u);
    if abs(m-m1)<ep
        break;
    end
    m1=m;
    
end
final_u=v;
final_x=p+1/m;
disp(A-p*I)
disp(final_u);
disp(final_x);