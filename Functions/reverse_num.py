def reverse(num):
    length=len(num)
    a=int(num)
    rev=0
    for i in range(1,length+1):
        d=a%10
        rev=rev*10+d
        a//=10

    print("The reversed num: ",rev)

reverse(input("Enter the number: "))        