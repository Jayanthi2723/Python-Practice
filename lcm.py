n1=int(input("enter the no:"))
n2=int(input("enter the no:"))
if n1>n2:
    g=n1
else:
    g=n2
while(True):
    if((g % n1 == 0) and (g % n2 == 0)):
        lcm=g
        break
    g +=1
print("LCM of",n1,"and",n2,"=",g)
