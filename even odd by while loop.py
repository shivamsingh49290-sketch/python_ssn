n=int(input("Enter a number: "))
m=int(input("Enter a number: "))
even=odd=0
i=n
if n<=m:
    while i <= m:
        if i % 2 == 0:
            print(f"{i} even")
            even = even + i
        else:
            print(f"{i} odd")
            odd = odd + i
        i=i+1
    print("sum of even numbers:" , even)
    print("sum of odd numbers:" , odd)
else:
    while i >= m:
        if i % 2 == 0:
            print(f"{i} even")
            even = even + i
        else:
            print(f"{i} odd")
            odd = odd + i
        i=i-1
    print("sum of even numbers:", even)
    print("sum of odd numbers:", odd)
