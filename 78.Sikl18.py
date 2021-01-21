import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
for i in range (a,b+1,2):
    m=a**b+b**i+c**a
    n=2*(i**2)+3*(a**i)
    y=y+m/n
print("%.2f" %y)