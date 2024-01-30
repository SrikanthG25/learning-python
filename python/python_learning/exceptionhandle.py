'''

try:
    a=int(input("value : "))
    b=int(input("value : "))
    c=input("value : ")
    print(c+b)

except ValueError as v:
    print("error the value ",v)
except TypeError as t:
    print("error the type ",t)
finally:
    print("error")

'''

try:
    f=open("file.txt","r")
except Exception as a:
    print(a)

finally:
    print("open successful")