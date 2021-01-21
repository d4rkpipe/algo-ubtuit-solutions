a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=5
while 5<=i<=10 :
    m=a**2+b*i+i**c
    n=a**2+b**2+i**2
    y=y+m/n 
    i=i+0.5
print("%.2f" %y)