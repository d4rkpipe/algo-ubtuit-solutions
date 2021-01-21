import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
y=0
i=d
while d<=i<=c :
    m=(a*i+b)/b**2+(math.cos(i))**2
    n=((math.sin(i))**2)/a*b
    y=y+m**(1/5)-n
    i=i+1.5
print("%.2f" %y)