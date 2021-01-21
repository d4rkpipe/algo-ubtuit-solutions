import math 
x=int(input('x='))
y=int(input('y='))
a=int(input('a='))
b=int(input('b='))
s=0
p=1
s1=0
p1=1
for k in range (1,x+1):
    s=s+(k**2+math.sin(k)+5)/(k**7+1)**(1/5)
print("%.2f" %s)
for n in range (1,y+1):
    p=p*((n+n**0.5)/n-(n+1)**0.2)
print("%.2f" %p)
for k in range (1,a+1):
    for i in range (1,b+1):
        p1=p1*(i**2+k**(2/i))/(math.sin(i)+math.cos(k))*i**k
    s1=s1+p1
print("%.2f" %s1)

