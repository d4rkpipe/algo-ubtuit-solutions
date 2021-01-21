import math 
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=-1
while -1<=i<=1 :
    m=math.sin(a*i)+b**c
    n=b**2+(math.cos(i))**2
    k=math.sin(i**2)
    p=a*b
    y=y+(m/n)**(1/3)-k/p
    i=i+0.25
print("%.2f" %y)