import math 
a=int(input('a='))
b=int(input('b='))
y=0
i=1
while 1<=i<=12 :
    y=y+(a**2+((b+math.sin(i))/(a**3+math.cos(i**3)*math.cos(i**3)))**0.2)
    i=i+2
print("%.2f" %y)


