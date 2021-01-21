a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=1
while 1<=i<=20 :
    m=a*(i**2)+b*i+c
    n=a**2+b**2+i**2
    y=y+m/n
    i=i+5
print("%.2f" %y)