"""
 
#A="srikanth"
#print(A.upper())

a=max(flase,-3,-4)
b=min(a,2,7)
print(b)


a=[1,2,3]
b=a
print(a is b,a==b)


#class
class fort:
    visit=""
    def tourist(self):
        print("must visit")
    def work(self ):
        print("profession")
ram = fort()
sri = fort()
ram.tourist()


# pattern 
n=int(input("Enter the value : "))
res=""
for i in range(0,n):
    for j in range(0,n):
        if j==0 or j==n-1 or ((i==j) and (j>0 and j<3)) or (i==1 and j==3) or i==2 and j==4 :
            print("*",end=" ")
        else:
            print(end="  ")
    print()


n=int(input("Enter the value : "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")   
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\n")




str1 =input("Enter the char : ") 
x = ""  
for i in str1:  
    x += i  
    print(x)



a = int(input("Enter the number of A : "))   
n = 1  
for i in range(a, 0, -1):  
    for j in range(1,i): 
        print(j, end=' ')  
    print()  



#prime 
a=int(input("Enter  the value : "))
if all(a%i!=0 for i in range(2,a)):
    print("Prime No")
else:
    print("not prime")


#factorial
a=int(input("Enter  the value : "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)


#factors
a=int(input("Enter  the value : "))
for i in range(1,a+1):
    if a%i==0:
        print(i)


#even or odd
a=int(input("Enter  the value : "))
if a%2==0:
    print("Even")
else:
    print("Odd")


#leapyear
def leapyear(n):
    if(n%400==0 or n%100!=0 and n%4==0):
        return "leapyear"
    else:
        return "not leapyear"
a=int(input("Enter the value : "))
print(leapyear(a))

#pattern
n=int(input("Enter the Value : "))
for i in range(0,n):
    for j in range(0,i+1):
        print("^",end="   ")
    print("\n")
#reverse
n=int(input("Enter the Value : "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("^",end="   ")
    print("\n")
   
#number pattern
n=int(input("Enter the Value : "))
#num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="   ")
    print("\n")

n=int(input("Enter the Value : "))
#num=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="   ")
    print("\n")
    

#char pattern
n=int(input("Enter the Value : "))
char=65
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(char)
        print(ch,end="   ")
        char +=1
    print("\n")


#reverse a string without string fun
def rev(a):
    s=""
    for i in a:
        s=i+s
    return s
a=input("Enter a string : ")
print(rev(a))


a=input("Enter a string : ")
s=""
for i in a:
    s=i+s
print(s)


a=input("Enter a string : ")
print(a[::-1])


#palindrome
def pal(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
s=input()
print(pal(s))



"""



"""
#list
n=int(input())
list=[]
for i in range(n):
    m=int(input())
    list.append(m)
print(list)
print(len(list))
list.append(25)
print(list)
list.reverse()
print(list)
list.insert(0,"sri")
del list[2]
print(list)




#random module
import random
print(random.randint(1,99))



#map function
def sqrt(a):
    return a*a

list1=[]
num=int(input("size : "))
for i in range(num):
    ele=int(input())
    list1.append(ele)
print(list1)
for i in list1:
    print(i)

list1=list(map(sqrt,list1))
for i in list1:
    print(i)


#lambda function
list1=[]
num=int(input("size : "))
for i in range(num):
    ele=int(input())
    list1.append(ele)
print(list1)
for i in list1:
    print(i)

list1=list(map(lambda a:a*a,list1))
for i in list1:
    print(i)


#type caste
a=['1','2','5']
a=list(map(int,a))
print(a)
print(type(a[0]))


#filter function
d  
list1=[]
num=int(input("size : "))
for i in range(num):
    ele=int(input())
    list1.append(ele)
print(list1)

list1=list(filter(fil,list1))
print(list1)


#reduce function

from functools import reduce

list1=[]
num=int(input("size : "))
for i in range(num):
    ele=int(input())
    list1.append(ele)
print(list1)

#list1=reduce(lambda a,b:a+b,list1)
list1=reduce(lambda a,b:a-b,list1)
#list1=reduce(lambda a,b:a*b,list1)
#list1=reduce(lambda a,b:a/b,list1)
print(list1)




#string slicing

a="hp lap | rs=59000 | new "
print("brand : ",a[:a.index("|")])
print("rs : ",a[a.index("|")+1:a.rindex("|")])
print("condition : ",a[a.rindex("|")+1:])



try:
    a=int(input("value : "))
    b=int(input("value : "))
    print(a/b)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
finally:
    print("error")




import _thread
import time

def a(msg):
    count =0 
    while count<5:
        count +=1
        time.sleep(3)
        print(msg)
def b(msg):
    count =0 
    while count<5:
        count +=1
        time.sleep(5)
        print(msg)

try:
    _thread.start_new_thread(a,("Fun A"))
    _thread.start_new_thread(a,("Fun B"))
except:
    print("Error while starting thread")

while 1:
    pass

"""

import calendar
year=int(input("Enter the year : "))
print(calendar(year))
