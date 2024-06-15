base=int(input("enter a base number"))
exponent=int(input("enter exponent"))
result=1
print(base,"to power",exponent,"=",end="")
for exponent in range(exponent,0,-1):
    result*=base
print(result)
