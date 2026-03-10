from math import *
# 1-kasrning suratini a
# 1-kasrning maxrajining 1-ifodani b
# 1-kasrnig maxrajining 2-qismini suratini c
# 1-kasrning maxrajining 2-qismining maxrajini 2-ifodasini e
# 1-kasrga qo'shiluvchini f
# deb belgilab olamiz
x=float(input('x='))
y=float(input('y='))
a=x**2+1
b=x**2
c=x*y+y**2
e=y**2+(y**2+x*y)/(abs(x*y)+5)
f=1+cos(x)+1/sin(abs(x))
T11=a/(b+c/e)+1/f
print("%.2f"%T11)


