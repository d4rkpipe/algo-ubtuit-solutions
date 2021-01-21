import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
for i in range (a,c+1,3) :
    m=a*i+b
    n=b**2+(math.cos(i))**2
    k=math.sin(i**2)
    p=a*b   
    y=y+((m/n)**(1/3))-k/p
print("%.2f" %y)
