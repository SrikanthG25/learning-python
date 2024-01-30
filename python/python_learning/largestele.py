list=[]
n=int(input("Enter the value : "))
for i in range(n):
    ele=int(input("value : "))
    list.append(ele)
    list.sort()
print(list)
print(max(list))
print(min(list))