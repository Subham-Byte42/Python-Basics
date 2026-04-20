   #Take marks as input and print grade:  90+ → A, 75–89 → B,  50–74 → c,  Below 50 → Fail

marks=int(input("Enter marks:"))
if(marks>90):print("A")
elif(75<marks<89):print("B")
elif(50<marks<74):print("C")
else:print("Fail")
