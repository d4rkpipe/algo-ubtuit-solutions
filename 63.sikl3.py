import time
n=int(input('n='))
p=1
s=0
k=-1
for i in range (1,2*n) :

    p=p*i

    if i%2==0:
        p=p*k
    else:
        s=s+1/p
    time.sleep(2)
  
print("%.4f" %s)
