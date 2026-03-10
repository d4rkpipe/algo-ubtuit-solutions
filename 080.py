import math 
a=int(input('a='))
y=0
i=0
while 0<=i<=10 :
    y=y+a*math.cos(i)-math.sin(i**2)
    i=i+0.5
print("%.2f" %y)