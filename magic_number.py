n=int(input("enter a number "))
sum=0
mul=1
a=0
while n>0:
    a=n%10
    mul = mul * a
    sum = sum + a
    n=n//10
if sum == mul:
     print("magic number")
else:
    print("not a magic number")