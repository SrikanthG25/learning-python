
# letfangle triangle
n=5
k=8
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("*",end=" ")
    print()

def pat(x):
    a=0
    for i in x:
        a=a+1
        print(x[:a])
    for i in x:
        a=a-1 
        print(x[:a])
pat("Srikanth")

#pyramid
def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i)+" *"*(i))
pattern(5)

def pattern(n):
    for i in range(1,n+1):
        print(" "*(i-1), end=" ")
        print("*"*(2*(n-i)+1))
pattern(5)

m=5
a=0  
n=bool(a)
if n==True:
    for i in range(1,m+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    for i in range(m+1,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

