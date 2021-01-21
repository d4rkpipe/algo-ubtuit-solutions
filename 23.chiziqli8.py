from math import *
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
x=float(input('x='))
# ifodaning  1-qismi kasrning suratini m
# 1-qismi maxrajini n
# 2-qismi kasrning suratini k
# 2-qismi maxrajini p
# deb belgilab olamiz
m=a*x**2+b*x+c
n=x*(a**3)+a**2+a**(b-c)
k=a*x+b
p=c*x+d+2**c
Y2=m/n+cos(abs(k/p))
print("%.2f"%Y2)
