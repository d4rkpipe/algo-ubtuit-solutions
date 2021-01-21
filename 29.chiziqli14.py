from math import *
# describe the constant 
e=2.718
a=int(input('a='))
x=float(input('x='))
y=float(input('y='))
# ifodaning 2-ildiz ostidagini m
# ifodaning birinchi ildizini n
# qo'shiluvchini k
# deb belgilab olamiz
m=(e**x+a/(x**2+2))**0.5
n=y**2+e**x+cos(x)*cos(x)/(sin(x**2))
k=cos(x)*cos(x)*cos(x)
TT=((n+m)**0.5)+k
print("%.2f"%TT)

