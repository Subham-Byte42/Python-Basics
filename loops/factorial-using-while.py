num=int(input("Enter num whose factorial you wanna find:"))

fact=1
# for i in range(1,num+1):      //by using for loop
#     fact=fact*i

while(num>0):
    fact=fact*num
    num-=1
    

print("Factorial: ",fact)