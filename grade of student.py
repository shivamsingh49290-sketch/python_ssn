a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
e=int(input("Enter a number"))
if a<=100 and b<=100 and c<=100 and d<=100 and e<=100:
    if a>=0 and b>=0 and c>=0 and d>=0 and e>0:
        sum = a + b + c + d + e
        print(sum)
        percentage = (sum / 500 * 100)
        print(percentage)
        if percentage < 33:
            print("fail")
        elif percentage <= 33 and percentage > 45:
            print("third division")
        elif percentage <= 45 and percentage > 60:
            print("second division")
        else:
            print("first division")

    else:
        print("check the entered number is in negative ")
else:
    print("check the entered number exceeds more than 100 ")