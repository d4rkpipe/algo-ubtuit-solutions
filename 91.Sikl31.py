import math 
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1
s1=0
p1=1
for m in range (1,a+1):
    s=s+(3*(m**3)+4*m+5)/m**3+math.log(m,math.e)
print("%.2f" %s)
for k in range (1,b+1):
    p=p*k/(k**3+7*k+5)
print("%.2f"%p)
for i in range (1,c+1): 
    for m in range (1,d+1):
        p1=p1*(math.log(i,math.e)+m**i)/m**i
    s1=s1+p1
print("%.2f"%s1)