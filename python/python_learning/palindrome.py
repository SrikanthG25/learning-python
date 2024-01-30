#string
# user=input("Enter the value : ")
# if user==user[::-1]:
#     print("the {} is palindrome".format(user))
# else:
#     print("the {} is not palindrome".format(user))

#integer
num=int(input("Enter the value : "))
temp=num
r=0
while(num>0):
    dig=num%10
    r=r*10+dig
    num=num//10
if temp==r:
    print("palindrome")
else:
    print("not palindrome")