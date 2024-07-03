

# Map function
# l=['1','2','3','4','5']
# l=list(map(float,l))
# print(type(l[2]),l)

# print(type(l[2]))
# for i in range(0,5):
#     l[i]=int(l[i])
# print(type(l[2]))


# typecasting str
# l=['1','2','3','4','5']
# l=list(map(int,l))
# for i in l:
#     print(i*i)


# #list square 
# l1=[25,1,5,7,95,35,25]
# l1=list(map(lambda l1:l1*l1,l1))
# print(l1)
# for i in l1:
#     print(i)



#filter function
# def greater(n):
#     return n>25
# l1=[25,1,5,71,95,35,25]
# l1=list(filter(greater,l1))
# print(l1)




# from functools import reduce
# l1=[25,1,5,71,95,35,25,3]
# l1=reduce(lambda a,b:a+b,l1)
# print(l1)

'''
n=0
for i in l1:
    n+=i
print(n)

'''

# s = 'srikanth'
# sr = s.swapcase()
# print(s)

x = [9, 8, 7, 6]
x[2] = 1
x[x[2]] = 5
print(x[1] % 3)