'''
# _thread 
import _thread
import time

def a(msg):
    count = 0
    while count < 5:
        count +=1
        time.sleep(2)
        print(msg)

def b(msg):
    count = 0
    while count < 5:
        count +=1
        time.sleep(4)
        print(msg)

try:
    _thread.start_new_thread(a, ("Function A",))
    _thread.start_new_thread(b, ("Function B",))

except:
    print("Error to start threat")
while 1:
    pass
    

#threading...
import threading
import time
def display(a,t,name): #getting arguments
    for i in range(a):
        time.sleep(t)
        print(name,"::Thread start")
t=threading.Thread(target=display , args=(5,1,"thread_1")) #passing arguments
t.start()
t1=threading.Thread(target=display , args=(5,1,"Thread_2"))
t1.start()


# set thread name 
import threading , time
def var(x):
    for i in range(5):
        time.sleep(x+1.5)
        print(threading.current_thread().getName()) # to get thread name
        print("thread started")w
for a in range(4):
    t=threading.Thread(target=var , args= (a,))
    t.setName("thread # " + str(a))  # to set thread name 
    t.start()



# thread is alive or not
import threading , time 
def var1(i):
    time.sleep(i)
    return

t1=threading.Thread(target=var1 , args=(1,) , name="thread#1")
t1.start()
t2=threading.Thread(target=var1 , args=(2,) , name="thread#2")
t2.start()

for x in range(5):
    time.sleep(x+0.5)
    print('[',time.ctime(),t1.name,t1.is_alive(),']')
    print('[',time.ctime(),t2.name,t2.is_alive(),']')



#daemon thread

import threading , time

def Emp1():
    print("thread_1 started")
    time.sleep(10)
    print("thread_1 finish")
def Emp2():
    print("thread_1 started")
    print("thread_2 finish")
t1= threading.Thread(target=Emp1 , daemon=True) #to declare daemon thread
t2= threading.Thread(target=Emp2)
t1.start()
t2.start()
t1.join() #to check end the daemon thread
t2.join() 



import threading , time
def Emp1():
    print("thread start")
    print(threading.current_thread()) #to check thread running
    time.sleep(5) #to end the thread
def Emp2():
    time.sleep(10)
t1=threading.Thread(target=Emp2 , daemon=True)
t1.start()
for i in range(5): 
    t=threading.Thread(target=Emp1)
    t.start()
    time.sleep(1)
print("enumerate : ",threading.enumerate())
print("Total thread count : " , threading.active_count())


#sub class threading

import threading
class thread(threading.Thread):
    def run(self):
        print("Untold")
        self.new()
        return
    def new(self):
        print("Mystery")
for i in range(5):
    t=thread()
    t.start()


#argument passing
class thread_cls(threading.Thread):
    def __init__(self , args=(),kwargs=None):
        threading.Thread.__init__(self)
        self.args=args
        self.kwargs=kwargs
    def run(self):
        print("thread" , self.args,"Argument is ",self.kwargs)
        return
for i in range(5):
    t1=thread_cls(args=(i,),kwargs = "hello")
    t1.start()

#timer threading in python

import threading , time

def demo():
    print("Welcome")
for i in range(5):
    t=threading.Timer(3.0 , demo)
    t.start()
    time.sleep(2) #to cancel thread in 2s 
    print("Thread canceled")
    t.cancel()

#Event Object

import threading , time 
def eventSet():
    time.sleep(2)
    event.set()
    print("Event is set")
    time.sleep(10)
    event.clear()
    print("Event is clear")
def eventOperation():
    event.wait()
    while event.is_set():
        time.sleep(1)
        print("Thread is waiting for signal")
    print("Thread is received signal")
event=threading.Event()
t1=threading.Thread(target=eventSet)
t2=threading.Thread(target=eventOperation)
t1.start()
t2.start()
t1.join()
t2.join()


# synchronizing thread lock() , acquire() , release()
import threading , time
lock=threading.Lock()
def runthread(name):
    time.sleep(1)
    lock.acquire()
    display(name)
    lock.release()
def display(name):
    for i in range(5):
        time.sleep(2)
        print(name,"Executed : value of i is " , i)
t1=threading.Thread(target=runthread,args=("Thread 1",))
t2=threading.Thread(target=runthread,args=("Thread 2",))
t3=threading.Thread(target=runthread,args=("Thread 3",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

'''
#RLock()
import threading
class thread():
    def __init__(self):
        self.a=5
        self.b=10
        self.Lock = threading.RLock()
    def first(self):
        print("Enter into first")
        with self.Lock:
            self.a +=5
    def second(self):
        print("Enter into second")
        with self.Lock:
            self.b -=5 
    def main(self):
        print("Enter into Main")
        with self.Lock:
            self.first()
            self.second()
            print(self.a,self.b)

obj=thread()
obj.main()
