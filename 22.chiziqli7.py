from math import * 
x1=float(input('x1='))
x2=float(input('x2='))
c=int(input('c='))
d=int(input('d='))
# ifodaning 1-qismining kasrini m
# 1-qismining maxrajini n
# 2-qismini  k
# deb belgilab olamiz
m=sin(abs(c*x2**3+d*x1**3-c*d))*sin(abs(c*x2**3+d*x1**3-c*d))
n=(c*x1**2+d*x2**2+7)**0.5
k=tan(x1*x2**2+d**3)
F= abs(m/n)+k
print("%.2f"%F)
