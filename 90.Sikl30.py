import math 
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=-math.pi
while -math.pi<=i<=math.pi :
    m=(math.log(a**(2*math.sin(i)),math.e)+math.e**(2*i))/math.atan(i)+b
    n=c
    i=i+0.25
    y=y+m+n
    i=i+math.pi/10
print("%.2f" %y)