def count(num):
    a=int(num)
    i=1
    count=0
    while(a!=0):
        d=a%10
        count+=1
        a//=10
        i+=1

    print("Number of digits: ",count)


count(input("Enter the number: "))    
