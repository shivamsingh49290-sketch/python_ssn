num=int(input("Enter a number:"))
m=0
i=2
while i<num:
    if num%i==0:
        m=1
        break
    i=i+1
if m==0:
    print("prime number")
else:
    print("not a prime number")