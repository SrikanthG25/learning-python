def fibo(a):
    x=0
    y=1
    print(x)
    print(y)
    for i in range(2,a):
        z=x+y
        x,y=y,z
        print(z)     
fibo(8)