a=float(input('a='))
if     a<=-1 :
        y=-a 
elif -1<=a<=0 :
        y=a+1
elif 0<=a<=1 :
        y=1-a 
elif 1<=a :
        y=a-1 
print("%.2f" %y)
