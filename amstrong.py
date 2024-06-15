n=int(input("number"))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum+=a**3
    temp//=10
if n==sum:
   print("amstrong num")
else:
   print("not amstrong")
