from math import * 

x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))

s=0
p=1
s1=0
p1=1
for k in range (1,x+1):
    s1=s1+k**3+e**k
print("%.2f" %s)
for a in range (3,y+1):
    p1=p1*(a*x)/(a**2+x**2)**0.5
print("%.2f" %p1)
for i in range (1,c+1):
    for j in range(1,d+1):
        p1=p1*(i*x+j**2)/(i**2+j*y)**0.5
    s1=s1+p1
print("%.2f" %s1)
