num=int(input("Enter the number of terms: "))
a=0
b=1
print(a,"",b,end="")                #in python end="" is used to add the lines
for i in range(2,num,1):
    next=a+b
    print("",next,end="")
    a=b
    b=next
   