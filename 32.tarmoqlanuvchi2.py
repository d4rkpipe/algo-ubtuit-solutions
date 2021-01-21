x=float(input('x='))
y=float(input('y='))
z=float(input('z='))
max=x
min=0
if x>y:
    max=x
    min=y
elif x<y:
    max=y
    min=x
if z>max:
    max=z
if z<min:
    min=z
    print(max,min) 
else :
    print(max,min)