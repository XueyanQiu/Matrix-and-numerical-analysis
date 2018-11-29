x = [0;0];
A = [6,3;3,2];
b = [0;-1];
r = b - A * x;
p = r;
i = 0;
while (~all(r == [0;0])) && (~all(dot(p, A * p) == [0;0]))
    alpha = dot(r, r) / dot(p, A * p);
    xx = x + alpha * p;
    rr = r - alpha * A * p;
    beta = dot(rr, rr) / dot(r, r);
    pp = rr + beta * p;
    i =i+1 ;
    r = rr;
    x = xx;
    p = pp;
end
disp(x);