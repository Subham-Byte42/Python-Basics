num=int(input("Enter the num to check:"))
a=num
arm=0
length=len(str(num))
while(num!=0):
    d=num%10
    arm=arm+pow(d,length)
    num//=10

if a==arm:print("It is a armstrong number.")
else:print("Not armstrong")    

