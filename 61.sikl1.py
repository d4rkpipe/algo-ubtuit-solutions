# Python Program to calculate Sum of Series
import math 
n = int(input("n="))
s = 0.0
for i in range(1,n+1) :
    s=s+math.sin(i)/2**i
print('%.2f'%s)