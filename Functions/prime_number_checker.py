def prime(num):
    a=int(num)
    prime=True
    for i in range(2,a):
        if a%i==0 :prime=False

    if prime :print("Prime Number") 
    else:print("Not a prime number")

prime(input("Enter num to check: "))       
