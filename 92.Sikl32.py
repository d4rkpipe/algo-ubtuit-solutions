import math 
x=int(input('x='))
y=int(input('y='))
a=int(input('a='))
b=int(input('b='))
s=0 
p=1
s1=0
p1=1
for a in range (1,x+1):
    s=s+(a**2+2*a)/a**3+a*(math.cos(a))**2+1
print("%.2f" %s)
for i in range (1,y+1):
    p=p*(i**2+1)/i**(3/i)+2
print("%.2f" %p)
for i in range (1,a+1):
    for k in range (1,b+1):
        p1=p1*math.log((k**i+k**(1/i))/k**3+i**(1/k),math.e)
    s1=s1+p1
print("%.2f" %s1) 