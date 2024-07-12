wrd=input("Enter a string : ")
c={}
for i in wrd:
    if i not in c:
        c[i]=0
    c[i]+=1
print(c)


wrd = input("Enter a string : ")
c = []
for i in wrd:
    if i not in c:
        c.append(i)
        c.append(1)
    else:
        idx = c.index(i)
        c[idx + 1] += 1
print(c)