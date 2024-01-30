'''
list=[25,1,5,7,95,35,25]
for i in list:
    print(i)


name="srikanth"
for i in name:
    print(i)

for i in 'sri':
    print(i,end=" ")

for i in range(0,11):
    print(i)

for i in range(11,0,-1):
    print(i)

for i in range(1,100):
    if i%2==0:
        print(i)


a=5
b=10
print("a > b") if a>b else print("a < b")
'''

#time module

import time
initial=time.time()
for i in range(25):
    print("Untold_Mystery")
    time.sleep(2)
print("total time : ",time.time()-initial)
initial1=time.time()
a=0
while a<25:
    print("Untold_Mystery")
    a=a+1
print("total time : ",time.time()-initial1)


print("Current Time : ",time.asctime(time.localtime(time.time())))