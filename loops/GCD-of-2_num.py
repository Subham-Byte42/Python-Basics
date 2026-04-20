num1=int(input("Enter the first num: "))
num2=int(input("Enter the second num: "))
gcd=1
i=2
while i<=(min(num1,num2)):
    if(num1%i==0 and num2%i==0):gcd=i
    i+=1

print("The GCD of these two nums: ",gcd)    
