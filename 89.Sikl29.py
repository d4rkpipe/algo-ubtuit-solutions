import math 
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=0
while 0<=i<=1 :
    m=((math.sin(a*i)+b**c)/b**2+(math.cos(i))**2)**0.5
    n=(math.sin(i**2))/a*b
    y=y+m-n
    i=i+0.25
print("%.2f" %y)
