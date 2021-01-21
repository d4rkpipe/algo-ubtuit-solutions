x=float(input('x='))
y=float(input('y='))
if y<=2*x+3 and y>=0 and y<=-x :
    print('YES')
elif  y<=2*x+3 and y>=1/3*x-1/3 and y<=0 :
    print('YES')
else:
    print('NO')


