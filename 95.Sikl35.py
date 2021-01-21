import math 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1
s1=0
p1=1
for i in range (1,x+1):
    s=s+(i**4+i**2+3)/(i+math.e**i)**0.5
print("%.2f" %s)
for k in range (1,y+1):
    p=p*(k+1)/k**3+5*k
print("%.2f" %p)
for m in range (1,c+1):
    for n in range (1,d+1):
        p1=p1*(abs(m**n-n**m)/m**n+n**m)**0.5
    s1=s1+p1
print("%.2f" %s1)