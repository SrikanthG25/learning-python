x=int(input("Enter the value x : "))
y=int(input("Enter the value y : "))
temp=x
x=y
y=temp
print("the  after swap of x is ",x)
print("the  after swap of y is ",y)


#without 3rd variable
x=int(input("Enter the value x : "))
y=int(input("Enter the value y : "))
x=x+y
y=x-y
x=x-y
print("the  after swap of x is ",x)
print("the  after swap of y is ",y)

x=int(input("Enter the value x : "))
y=int(input("Enter the value y : "))
x,y=y,x
print("the  after swap of x is ",x)
print("the  after swap of y is ",y)
