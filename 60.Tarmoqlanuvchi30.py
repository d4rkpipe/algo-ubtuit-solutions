import math
x=float(input('x='))
y=float(input('y='))
if 0<=x<=1 and -1<=y<=1 : 
    x**2+y**2<=1
    print('YES')
elif -2<=x<=0 and -1<=y<=1 :
    abs(x+1)>=-2 
    print('Yes')
else :
    print('NO')