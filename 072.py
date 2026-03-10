n=int(input('n='))
x=int(input('x='))
s=0
p=1
for i in range (1,2*n-1,2) :
    p=p*i
    s=s+(x**(p))/p
print(s)