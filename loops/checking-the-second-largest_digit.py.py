#here we are finding the second largest digit in a number,and also it is a good logic

num=input("Enter the num: ")

largest=second=-1

for d in num:
    d=int(d)
    if(d>largest):
        second=largest
        largest=d
    elif(d>second and d!=largest):
        second=d

if second==-1:print("No second largest digit")
else:print("second largest digit: ",second)            