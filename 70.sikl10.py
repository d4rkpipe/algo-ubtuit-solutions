import time
n=int(input('n='))
x=int(input('x='))
p=1
s=0
k=-1
for i in range (1,2*n) :
    p=p*i
    if i%2==0:
        p=p*k
    else:
        s=s+x**i/p
    time.sleep(1)
  
print("%.3f" %s)