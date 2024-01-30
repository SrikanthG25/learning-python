num=int(input("Enter the value : "))
if all(num%i!=0 for i in range(2,num)):
    print("the given number {} is prime No.".format(num))
else:
     print("the given number {} is Not a prime No.".format(num))