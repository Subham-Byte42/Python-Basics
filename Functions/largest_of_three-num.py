def largest(num1,num2,num3):
    a=int(num1)
    b=int(num2)
    c=int(num3)
    lar=a
    if(b>a and b>c):lar=b
    elif(c>a and c>b):lar=c

    print("Largest num: ",lar)

largest(input("Enter num1: "),input("Enter num2: "),input("Enter num3: "))    