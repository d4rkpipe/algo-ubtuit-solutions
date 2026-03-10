#defin the constant
e=2.71
from math import *
x=float(input('x='))
y=float(input('y='))
# kasrning qo'shiluvchisini a
# kasrning maxrajini b
# ayiriluvchini c
# deb belgilab olamiz
a=(x**3/((x**4)+2*x+3))+e**((x**2)+3*x)
b=atan(x+y)+abs(5+x)**2
c=cos(y**2+(x**2)/2)*cos(y**2+(x**2)/2)
f1=a/b-c
print("%.2f"%f1)
