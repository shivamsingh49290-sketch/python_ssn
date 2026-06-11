
a=float(input("enter a number"))
b=float(input("enter a number"))
c=float(input("enter a number"))
import math  as m
import cmath as cm
d=(b*b)-(4*a*c)
if d<0:
    print("no real roots")
    x1 = ((-b + cm.sqrt(d)) / (2 * a))
    x2 = ((-b - cm.sqrt(d)) / (2 * a))
    print("x1=", x1)
    print("x2=", x2)
elif d==0:
    print("real and equal roots")
    x1=x2=-b/(2*a)
    print("x1=" , x1 , "x2=" , x2)
else:
    x1=((-b + m.sqrt(d))/(2*a))
    x2=((-b - m.sqrt(d))/(2*a))
    print("x1=" , x1)
    print("x2=" , x2)