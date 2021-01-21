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
if x+y+z>max:
    max=x+y+z
if x+y/2<min:
    min=x+y/2
print(max,min**2)
