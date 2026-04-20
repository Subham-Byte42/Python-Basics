def armstrong(num):
    length=len(num)
    a=int(num)
    b=a
    i=1
    sum=0
    while a!=0:
        d=a%10
        sum=sum+pow(d,length)
        a//=10
        i+=1

    if b==sum:print("Armstrong number")
    else:print("Not armstrong num") 

armstrong(input("Enter num to check: "))      

