from math import *
e=2.718
x=int(input('x='))
y=int(input('y='))
# o'nli logarimning modulidagi birinchi qismni a deb olamiz
# ikkinchisini b deb olamiz
# uchinchisi c deb olamiz
# qo'shiluvchini d 
# deb belgilab olamiz
a=(x+y)**2
b=(abs(y)+2)**1/2
c=x-(x*y)/((x**2)/2-5)
d=cos(x+y)*cos(x+y)/(x+y)**(1/3)
z=log(abs(a+b-c),e)+d
print("%.2f"%z)