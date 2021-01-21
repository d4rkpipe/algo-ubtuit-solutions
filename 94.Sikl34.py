import math 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1
s1=0
s2=0
for a in range (1,x+1):
    s=s+(2*a+math.cos(a))**2
print("%.2f" %s)
for a in range (1,y+1):
    p=p*(a+6)/(a**2+2)**0.5
print("%.2f" %p)
for k in range (1,c+1):
    for y in range (1,d+1):
        s1=s1+(k**2+y)/((k**2+y**2)**.5)
    s2=s2+s1
print("%.2f" %s2)

