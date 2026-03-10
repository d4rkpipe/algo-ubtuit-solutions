import math 
a=int(input('a='))
y=0
i=-math.pi/2
while -math.pi/2<=i<=math.pi :
    m=(a)**(a/3)
    n=(i**2)*math.cos(a*i)
    y=y+m+n
    i=i+math.pi/19
print("%.2f" %y)