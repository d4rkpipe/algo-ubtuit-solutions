from math import * 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1
p1=1
p2=1
for a in range (1,x+1):
    s=s+(a*x+4)/(a+log(6,e))**0.5
print("%.2f" %s)
for a in range (1,y+1):
    p=p*(a*(x**2)+6)/sin(a*x)
print("%.2f" %p)
for i in range (1,c+1):
    for j in range(1,d+1):
        p1=p1*(i*j+y*x)/(j*x+y)**(i/2)
    p2=p2*p1
print("%.2f" %p2)
        
