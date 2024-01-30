num=12
#num=int(input("Enter the value : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)

num=12
#num=int(input("Enter the value : "))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum+=i
print("Total : ",sum)