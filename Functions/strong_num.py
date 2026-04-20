def strong(num):
    length=len(num)
    n=int(num)
    a=n
    sum=0
    for i in range(1,length+1):
        d=n%10
        fact=1
        for j in range(1,d+1):fact*=j
        sum+=fact
        n//=10
    
    if(sum==a):print("Strong Number")
    else:print("Not strong")

strong(input("Enter the number: "))    