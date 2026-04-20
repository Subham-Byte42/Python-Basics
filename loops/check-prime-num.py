a=int(input("Enter the num you want to check: "))
isprime=True
for i in range(2,a):                #here the start point is considered where as the end point is not considered
    if a%i==0:isprime=False

if isprime:print(a,"is a prime num.")
else:print(a,"is not a prime num.")    

         