f=open("fruits.txt","w")
#print(f)


f.write("banana\n")

#content=f.read()
#print(content)
f.close()
f=open("fruits.txt","r+")#read and write operation
print(f.read())

f=open("fruits.txt","a")#append
#print(f)


f.write("apple\n")
f.write("orange\n")

f=open("fruits.txt","r+")#read and write operation
print(f.read())
