x=float(input('x='))
y=float(input('y='))
z=float(input('z='))
minimum= min(x,y,z)
if   x<1 and y<1 and z<1:
    if x==minimum:
        x=(y+z)/2
    if y==minimum:
        y=(x+z)/2
    if z==minimum:
        z=(y+x)/2
    print(x,y,z)
else: 
    print(x,y,z)
