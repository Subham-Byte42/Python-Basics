def fab(num):
    n=int(num)
    print("0  1",end="")
    a=0
    b=1
    for i in range(3,n+1):
        next=a+b
        print(" ",next,end="")
        a=b
        b=next

fab(input("Enter the number of terms: "))        