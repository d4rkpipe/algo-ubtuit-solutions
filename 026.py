from math import *
a=int(input('a='))
x=float(input('x='))
y=float(input('y='))
# describe the constant
e=2.71
# ifodaning birinchi qismini m
# ifodaning ikkinchi qismini n
# deb belgilab olamiz
m=(e**(x*y)-x*sin(a*x)-(x**2+2)/abs(x)+5)**0.5
n=(log(x**2+2,e)+5)**0.5
W2=m+n
print("%.2f" %W2)
