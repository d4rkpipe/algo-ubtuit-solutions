import math
n=int(input('n='))
s=0.0
for i in range(1,n+1):
    if i%2==0:
        s=s-((math.sin(i**i))/2**i)
    elif i%2!=0:
        s=s+((math.sin(i**i))/2**i)
print('%.2f'%s)