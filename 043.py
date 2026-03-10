x=float(input('x='))
y=float(input('y='))
a=0
b=0
if x>0 :
    a=abs(x)
if y>0 :
    b=abs(y)
if x<0<=y :
    a=x+0.5
    b=y+0.5
if y<0<=x :
    a=x+0.5
    b=y+0.5
print(a,b) 