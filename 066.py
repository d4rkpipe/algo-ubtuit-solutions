import math
n=int(input('n='))
x=int(input('x='))
s=0.0
for i in range (1,n+1) :
    if i%2==0 :
        s=s-(1/i)*math.sin(i*x)
    elif i%2!=0 :
        s=s+(1/i)*math.sin(i*x)
print('%.3f'%s)
