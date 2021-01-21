import math
n=int(input('n='))
x=int(input('x='))
s=0.0
for i in range (1,n+1) :
    s=s+(x**i)/i**0.5
print('%.3f'%s)