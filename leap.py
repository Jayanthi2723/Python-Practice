n=int(input("enter the year"))
if((n%100) and (n%4)):
    print("leap year")
elif((n%400) and (n%100!=0)):
    print("leap year")
else:
    print("not leap year")
