#way1
a=float(input("enter a number"))
b=float(input("enter a number"))
c=float(input("enter a number"))
import cmath  as m
d=(b**2)-(4*a*c)
print("d=" ,d)
x1=((-b + m.sqrt(d))/(2*a))
x2=((-b - m.sqrt(d))/(2*a))
print("x1=" , x1)
print("x2=" , x2)



# way2 -
a=float(input("enter a number"))
b=float(input("enter a number"))
c=float(input("enter a number"))
import math  as m
d=(b**2)-(4*a*c)
if d<0:
    print("no real roots")
else:
    x1=((-b + m.sqrt(d))/(2*a))
    x2=((-b - m.sqrt(d))/(2*a))
    print("x1=" , x1)
    print("x2=" , x2)