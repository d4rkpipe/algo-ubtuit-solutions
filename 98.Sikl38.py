import math 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1 
s1=0
p1=1
for a in range (1,x+1):
    s=s+(4*a+6*math.log(a,math.e))/a**2+a
print("%.2f" %s)
for a in range (1,y+1):
    p=p*(abs(a-6*math.cos(a)))/a**2+a**math.log(a,math.e)
print("%.2f" %p)
for a in range (1,d+1):
    for k in range (1,c+1):
        p1=p1*(a*k+x)/k**2+y**2
    s1=s1+p1
print("%.2f" %s1)