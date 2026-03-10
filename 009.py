# python program to find the time of an object when it hits the ground after being dropped.
#define the constant
g=9.8
import math
h=int(input('h='))
t=math.sqrt(2*h/9.81)
print("%.2f" %t)
