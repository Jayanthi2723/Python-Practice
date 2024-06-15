first,second=0,1
n=int(input("enter series"))
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-1)
print("fibonacci series")
for i in range(0,n):
    print(fibonacci(i))
