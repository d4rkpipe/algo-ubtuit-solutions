import math 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1 
s1=0 
p1=1
for n in range (1,x+1):
    s=s+1/5-17*n+n**3
print("%.2f" %s)
for  m in range (1,y+1):
    p=p*(abs(m-5)+1)/m**2+4*m-1
print("%.2f" %p)
for i in range (1,c+1):
    for k in range (1,d+1):
        p1=p1*(-1**i)*(((math.sin(k)+math.e**k)**(1/7))/2*abs(4*i**3-k**4))
    s1=s1+p1
print("%.2f" %s1)