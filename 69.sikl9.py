n=int(input('n='))
x=int(input('x='))
s=0
p=1
k=-1
for i in range (1,n+1) :
    p=p*i
    if i%2==0:
        s=s+x**i/p
    else :
        s=s+(x**i/p)*k
print('%.3f'%s)