import math 
x=int(input('x='))
y=int(input('y='))
c=int(input('c='))
d=int(input('d='))
s=0
p=1
s1=0
p1=1
for k in range (1,x+1):
    s=s+(((-1)**k)*(k+1))/k**3+k**2+1
print("%.2f" %s)
for i in range (1,y+1):
    p=p*(i**3+abs(i-9))/math.log(i,math.e)+7*i
print("%.2f" %p)
for n in range (1,c+1):
    for m in range (1,d+1):
        s1=s1+((-1)**m)*((math.log(m+5,math.e))/m**(n+3)+n*m)
    p1=p1*s1
print("%.2f" %p1)