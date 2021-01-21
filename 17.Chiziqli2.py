from math import *
x=float(input('x='))
y=float(input('y='))
# kasrning suratini a
# kasrning maxrajini b
# qo'shiluvchisini c
# deb belgilab olamiz !
a=2*tan(x+pi/6)
b=1/3+cos(y+x**2)*cos(y+x**2)
c=log(((x**2)+2),2)
f1=a/b+c
print("%.2f"%f1)


