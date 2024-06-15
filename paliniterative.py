n=int(input("enter the number"))
rev,temp=0,n
while temp!=0:
    temp=temp//10
    rev=rev*10+temp%10
if rev==n:
    print("palindrome")
else:
    print("not a palindrome")
