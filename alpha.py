j=input("enter a sentence\n")
n=l=0
for s in j:
    if (((s.isalpha()) or (s.isnumber()))):
       print("alpha","numeric",n=n+1,l=l+1)