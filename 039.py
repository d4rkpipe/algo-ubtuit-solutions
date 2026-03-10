
x=int(input('x='))
y=int(input('y='))
a,b=0,0
if x>y :
    b=(x+y)/2
    a=2*y*x
if x<y :
    b=2*x*y
    a=(x+y)/2
print(a,"%.2f"%b)