from math import *
a=int(input('a='))
x=float(input('x='))
# Ushbu ifodaning kasr qismini m 
# ifodaning maxraj qismini n 
# deb belgilab olamiz.
m=(x-1)**0.5+(x+2)**0.5+log((a*x**2)**0.5+2,10)
n=((x+2)**0.5+(x+24)**0.5+x**5)**0.5
TT=m/n 
print("%.2f"%TT)
