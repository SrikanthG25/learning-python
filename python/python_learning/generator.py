'''

iterable - using for loop for  __iter__()
iterator - to print the valve in iterable  __next__()
iteration - 



a ="UNOLD _ MYSTERY"
s=[25,"August",08.2002]
# b=109 integer is not iterable 
for i in a:
    print(i)
for i in s:
    print(i)



s="UNTOLDMYSTERY"
print(s.__iter__())

'''
def num():
    a=10
    b=15
    c=a+b
    # return c # to use once the return value
    yield c  # - to use multipe return the value and only call it
    yield a
sum=num()
print(next(sum))
print(next(sum))


