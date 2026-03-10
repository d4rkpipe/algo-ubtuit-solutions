n=int(input('n='))
x=int(input('x='))
s=0
p=1
for i in range (1,n+1) :
    p=p*i
    s=s+x**i/p
print('%.3f'%s)
