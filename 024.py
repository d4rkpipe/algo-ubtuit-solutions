from math import *
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
x=float(input('x='))
# ifodaning 2-qism kasrning suratidagi 1-ifodani m
# 2-qism kasrning 2-ifodani n
# 2-qism maxrajini k
# deb belgilab olamiz
m=8.2*x**2
n=(abs(x**3+3*x)+cos(x-2))**0.5
k=a/4+b/3+c/2+1
W1=0.75+((m+n)/k)
print("%.2f"%W1)
