num = int(input("Enter the number: "))
l = 0

while num != 0:
    d = num % 10
    if d > l:
        l = d
    num //= 10              #here the sign "//" removes the last digit of the number

print("The largest digit in the num:", l)
