import math 
a=int(input('a='))
y=0
i=-math.pi/2
while -math.pi/2<=i<=math.pi:
    m=2*((a**(math.sin(2*i)))*(1/3))
    n=(i**2)*math.cos(a*i)
    y=y+2*m+n
    i=i+math.pi/10
print("%.2f" %y)