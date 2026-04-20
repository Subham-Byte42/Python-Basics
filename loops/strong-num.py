#strong number is a number whose sum of the factorials of digits is same as number
num=input("Enter the number to check: ")
length=len(num)
b=int(num)
a=int(num)
sum=0
for i in range(1,length+1):
    d=b%10
    fact=1
    for i in range(1,d+1):fact*=i
    sum+=fact
    b//=10

if sum==a:  print("Strong Num")
else:print("Not a strong num")  


