x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
if   y-z<x<y+z and x-z<y<x+z and  x-y<z<x+y  :
    print('Yes')
else :
    print('No')