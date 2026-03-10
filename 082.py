a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
y=0
i=1
while 1<=i<=10 :
    y=y+(a*(i**2))/b+i/c
    i=i+3
print("%.2f" %y)