num=int(input("Enter the num: "))
a=num
rev=0
while(num!=0):
    d=num%10
    rev=rev*10+d
    num//=10

if(rev==a):print("Palindrome")
else:print("Not palindrome")    