from math import *
a=int(input('a='))
x=float(input('x='))
# ifodaning 1-qismini m
# ifodaning 2-qism kasrining suratini n
# ifodaning 2-qism kasrining maxrajini k
# deb belgilab olamiz
m=x*sin(x/2+x/3+x/4)
n=log(x**2-2,10)+3**a
k=(cos(x+3)*sin(x+3))+8
BB1=m+n/k 
print("%.2f"%BB1)
