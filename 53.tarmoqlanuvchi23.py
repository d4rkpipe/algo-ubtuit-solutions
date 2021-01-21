x=float(input('x='))
y=float(input('y='))
if -2<=x<=2 and 0<=y<=1.5 :
    if -1<=x<=1 and y>abs(x) and y<=1:
        print('yes')
    if 1<=y<1.5:
        print('YES')
    else :
        print('NO')
else :
    print('NO')
    