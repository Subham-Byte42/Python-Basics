def fact(num):
    a=int(num)
    fact=1
    for i in range(1,a+1):fact*=i

    print("Factorial: ",fact)

fact(input("Enter num: "))    