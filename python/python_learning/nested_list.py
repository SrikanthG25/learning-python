'''
list=[[1,2,3,4],[11,12,13,14]]
#print(list[0][2])
for i in list:
    for j in i:
        print(j)


#sum of odd no and even no
list=[1,5,7,9,12,15]
even=[]
odd=[]
ad=0
sub=0
for i in list:
    if i % 2==0:
        even.append(i)
        ad=ad+i
    else:
        odd.append(i)
        sub=sub+i
print(ad)
print(sub)


list=[25,1,5,7,95,35,25]
list.sort()
print(list)
list1=[[11,2,3,4],[11,12,13,14]]
list1.sort()
print(list1)

#swap the variable in list with third variable
list=[25,1,5,7,95,35,25]
temp=list[0]
list[0]=list[3]
temp=list[3]
print(list)

#swap the variable in list without third variable

list=[25,1,5,7,95,35,25]
list[0],list[4]=list[4],list[0]
print(list)


list1=[[1,2,3,4],[112,12,13,14]]
#list1[0][0],list1[1][0]=list1[1][0],list1[0][0]
#list1[0][0],list1[1][0],list1[0][1],list1[1][1],list1[0][2],list1[1][2],list1[0][3],list1[1][3]=list1[1][0],list1[0][0],list1[1][1],list1[0][1],list1[1][2],list1[0][2],list1[1][3],list1[0][3]
for i in list1:
    if list1[0][0] or list1[1][0]==list1[1][0] or list1[0][0]:       
        print(i)


lst=[]
for i in range(100):
    if i%5==0:
        lst.append(i)
print(lst)
# list
lst=[i for i in range(100) if i%5==0]
print(lst)


#dictionary

d={i:f"item{i}" for i in range(25)}
print(d)

#generator
even=(i for i in range(50) if i%2==0)
print(type(even))
print(next(even))
for i in even:
    print(i)


''' 

food=["sweet","salt","normal"]
for s in food:
    print(s)
    if s=="extra":
        break
else:
    print("print successfully")


