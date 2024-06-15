base=int(input("enter a base number"))
exponent=int(input("enter exponent"))
result=1
print(base,"to power",exponent,"=",end="")
while exponent!=0:
    result=base*result
    exponent-=1
print(result)
