wrd=input("Enter a srt : ")
c={}
for i in wrd:
    if i not in c:
        c[i]=0
    c[i]+=1
print(c)