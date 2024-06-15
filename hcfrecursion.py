def gcd(num1,num2):
    if num2==0:
        return num1;
    return gcd(num2,num1%num2)
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print("hcf/gcd of",num1,"and",num2,"=",gcd(num1,num2))
