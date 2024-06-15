num=int(input("enter the number"))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
       print("not binary")
       break
    else:
       print("binary")
       break
