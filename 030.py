from math import *
# decribe the constant
e=2.718
x=int(input('x='))
y=float(input('y='))
z=float(input('z='))
# ifodaning 1-qismini m 
# ikkinchi qismini n
# uchinchi qismini k 
# deb belgilab olamiz
m=2**(-x)
n=(x+((abs(y)+2)**0.25))**0.5
k=((e**(x-1)/sin(z+2))+2)**(1/3)
AF=m*n*k
print("%.2f"%AF)
