from array import *
arr=array('i',[])

n=int(input("how many students in class"))
print("no of students=",n)

for i in range(n):
    marks=int(input("enter the marks"))
    arr.append(marks)
'''print("the max numebr is=", max(arr))
print("the min number is=", min(arr))
print(" sum of marks=", sum(arr))'''

for i in arr:
    print(i)
max=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max =arr[i]
print("max number",max)
min=arr[0]
for i in range (1,len(arr)):
    if arr[i]<min:
        min=arr[i]
print("min marks",min)


