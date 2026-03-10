n=int(input('n='))
x=int(input('x='))
s=0
p=1
k=-1
for i in range (n) :
        p=(p*x**2)*k
        s=s-1/p
print("%.3f" %s) 
