a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
d=float(input('d='))
maximum=max(a,b,c,d)
minimum=min(a,b,c,d)
if a<=b<=c<=d:
    a,b,c,d=maximum,maximum,maximum,maximum
else :
    a,b,c,d=minimum,minimum,minimum,minimum
print(a,b,c,d)