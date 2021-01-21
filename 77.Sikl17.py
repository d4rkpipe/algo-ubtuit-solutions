import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
y=0
for i in range (c,d+1,2) :
    m=math.sin(a*i)+b**(2*c)
    n=b**2+(math.cos(i))**2
    k=math.sin(i**2)
    p=a*b 
    y=y+((m/n)**(1/3))-k/p
print("%.2f" %y)