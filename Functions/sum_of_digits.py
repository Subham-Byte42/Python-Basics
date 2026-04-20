def sum(num):
    a=int(num)
    i=1
    sum=0
    while(a!=0):
        d=a%10
        sum=sum+d
        a//=10

    print("Sum of digits: ",sum)

sum(input("Enter the number: "))        