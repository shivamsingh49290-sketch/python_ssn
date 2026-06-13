n=int(input("enter the starting number"))
m=int(input("enter the ending  number"))
c=n

while c<=m:
    a=c
    sum=0
    while a>0:
        digit=a%10
        sum=sum+digit**3
        a=a//10
    if sum==c:
        print(c,"its a armstrong number")
    c=c+1
else:
    while c>=m:
        a=c
        sum=0
        while a>0:
            digit=a%10
            sum=sum+digit**3
            a=a//10
        if sum==c:
            print(c,"its a armstrong number ")
        c=c-1

