a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
e=int(input("Enter a number"))
sum=a+b+c+d+e
print(sum)
percentage=(sum/500*100)
print(percentage)
if percentage<33:
    print("fail")
elif percentage<=33 and percentage>45:
    print("third division")
elif percentage<=45 and percentage>60:
    print("second division")
else:
    print("first division")