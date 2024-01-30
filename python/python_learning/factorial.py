#num=int(input("Enter the value : "))
num=5
fact=1
for i in range(1,num+1):
    fact=i*fact
print("The {} factorial is : ".format(num),fact)


def fat(a):
    fact=1
    for i in range(1,a+1):
        fact=i*fact
        print("Factorial : ",fact)
fat(5)