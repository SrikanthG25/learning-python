'''
def fun():
    print("_Untold_Mystery_")
fun()

#argument passing
def fun(a,b):
    """this is a function"""#insdide the fun in 1st line is doc string 
    print(a+b)
fun(20,5)
print(fun.__doc__)


def bio(name,age):
    print(name)
    print(age)
bio("Sri",21)
bio(age=21,name="Sri")#key word


#variable length arugument to store multiple value in argu in parameter is defined as **.
def add(a,*b):#int to change the tuple
    for i in b:
        a=a+i
        print(a)
    print("the total is : ",a)
add(5,7,8,5,41,4)


def add(a,b):#int to change the list
    for i in b:
        a=a+i
        print(a)
    print("the total is : ",a)
add(5,[7,8,5,41,4])def



#keyword len argu in parameter is defined as **
def per(name,**other):
    print(name,other)
per("sri",age=21,state="TN")

def my_function(*kids):
  for i in kids:
    print("The youngest child is " + i)

my_function("Emil", "Tobias", "Linus")


#global and local variable
#global variable outside the function
a=25
def fun():
    #global a #change a global variable value
    global b
    b=14 #local variable in sidee the function
    print(b)
fun()

print(a)
print(b)


def evenodd(n):
    e=0
    O=0
    for i in n:
        if i%2==0:
            e=e+1
            print("even : ",i)
        else:
            O=O+1
            print("odd : ",i)
    print("No of Even : ",e)
    print("No of Odd : ",O)


l=[6,14,19,25,29,1]
evenodd(l)

'''
