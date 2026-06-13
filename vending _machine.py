n=int(input("How many toffee you want ?:"))
i=1
stock=100
while i<=n:
    if i<=stock:
        print("collect your toffee",i)
    else:
        print("out of stock")
        break
    i=i+1
else:
    print("Thankyou for visitning")