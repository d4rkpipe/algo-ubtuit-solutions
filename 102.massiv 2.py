import numpy as np
n=int(input('n='))

s=[]

for i in range(n):
    print('s[',i,']=',end='')
    qabul=float(input('qabul='))
    s.append(qabul)
# s=np.array([i for i in range(1,101)])
s=np.array(s)
a=float(input('a='))
b=float(input('b='))
kichik=min(s)
for i in range(len(s)):
    if a<=i<=b:
        s[i]=s[i]/float(kichik)

print(s)
