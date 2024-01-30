'''
r-reading
w-writing
x-cretae a fine is not exists
a -append,add more content at the end 
t - text mode
b - binary mode
+ - update

#read
s=open("file.txt","r")
print(s.read())
print(s.readline())
print(s.read(6))
s.close()

#write
s=open("file.txt","w")
s.write("welcome to darkness\n")
s.write("to night")
s.close()


#append
s=open("file.txt","a")
s.write("\n dfsfsddv")
s.close()

#tell - to get the position of File Handle
s=open("file.txt")
print(s.tell())
print(s.readline())
print(s.tell())
s.close()


s=open("file.txt")
print(s.readline())
s.seek(12)
print(s.readline())
print(s.tell())
s.close()

'''


#with block function

with open("file.txt") as f:
    print(f.readline())
s=open("file.txt")
print(s.readline())
