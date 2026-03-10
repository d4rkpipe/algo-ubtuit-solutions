n = int(input("n="))
x = int(input("x="))
s = 0
for i in range(1,n+1) :
    s=s+i/(x**(2*i))
print('%.3f'%s)