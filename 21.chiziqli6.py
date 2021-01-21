from math import *
# ifodaning 1-qismini x 
# ikkinchi qismini y
# uchinchi qismini z
# deb belgilab olamiz
a=float(input('a='))
b=float(input('b='))
x= a**(1/5)
y= (b*((a+b)/(2*b+a*b)))**0.25
z= a**2+b**2+2
T= x+y*z
print("%.2f"%T)