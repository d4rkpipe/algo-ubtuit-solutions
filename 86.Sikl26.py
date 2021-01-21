import math 
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=c
while c<=i<=b :
    m=(a**2)*math.cos(i)
    n=(math.sin(i))/2
    k=b*(i**2)
    y=y+m+n+k
    i=i+0.25
print("%.2f" %y)