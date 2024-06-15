n1=int(input("enter the no:"))
n2=int(input("enter the no:"))
if n1>n2:
    minimum=n1
else:
    minimum=n2
for i in range(1, minimum+1):
    if((n1 % i == 0) and (n2 % i == 0)):
        hcf=i
print("HCF of",n1,"and",n2,"=",hcf)
