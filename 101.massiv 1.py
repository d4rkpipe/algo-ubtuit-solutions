import numpy as np 
n=int(input('n='))
s=[]
for i in range(n):
    qabul=int(input('<<son kiriting>>'))
    s.append(qabul)
#s=np.array([i for i in range (1,101)])
s=np.array(s)
ortacha=sum(s)/len(s)
yangi_massiv=np.array([i for i in s if i<ortacha])
print(sum(yangi_massiv)/len(yangi_massiv))