n=input("enter a string\n")
length=len(n)
if n[-3:]=='ing':
   print(n+"ly")
elif n[-2:]=='ly':
   print(n+"ing")
else:
   print("les tha 3")