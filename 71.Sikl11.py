n=int(input('n='))
x=int(input('x='))
s=0
k=-1
p=1
for i in range (1,2*n-1,2) :
    s=s+(x**(2*i-2))/2
  
print("%.3f" %s)