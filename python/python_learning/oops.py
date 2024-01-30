''' 
class untold():
    # a=int(input("Enter the value : "))
    def story(self,story):
        print(story)
        self.story=story
    def story1(self):
        print("Every story having not a good end",self.story)
    def story2(self):
        print("Every story having not a bad end",self.story)
        
obj=untold()
obj.story("untold_mystery")
print(obj.story1())
print(obj.story2())
# print(untold.a)



class Student():
    cha='introvent'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        return f"Name is {self.name} and age is {self.age}"
    @classmethod
    def changecha(cls,new):
        cls.cha=new

    @classmethod
    def spliter(cls,string):
        return cls(*string.split("-"))
        # splitting=string.split("-")
        # return cls(splitting[0],splitting[1])
# sri = Student()
# untold=Student()
# sri.name="srikanth"
# sri.age=21
# sri.position="student"
# untold.name="Untold_Mystery"
# print(sri.name)
# print(untold.name)
# print(Student.cha)
# print(sri.__dict__)
# print(sri.data())
s=Student('sri',21)
s.changecha('sri')#change the value of class variable
sr=Student.spliter('srikanth-21')
print(s.data())
print(s.cha)
print(sr.data())



class Student():
    cha='introvent'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def data(self):
        return f"Name is {self.name} and age is {self.age}"
    @classmethod
    def changecha(cls,new):
        cls.cha=new
    @classmethod
    def spliter(cls,string):
        return cls(*string.split("-"))
        # splitting=string.split("-")
        # return cls(splitting[0],splitting[1])
    @staticmethod#built-in decorator that defines a static method in the class
    def let(str):
        print("This is : ",str)
s=Student('sri',21)
r=Student('rish',19)
s.changecha('sri')#change the value of class variable
sr=Student.spliter('srikanth-22')
print(s.data())
print(s.cha)
print(sr.data())
Student.let("rish")

#single inheritance
class database(Student):
    def __init__(self, name, age, position):
        self.name=name
        self.age=age
        self.Position=position
    def database1(self):
        return f"Name is {self.name} and age is {self.age} and position is {self.Position}"

san=database('sanjai',20,'student')
print(san.data())
print(san.database1())


#multiple inheritance
class play():
    __No_of_game=25 # private Access modifier
    def __init__(self,name,game):
        self.name=name
        self.gaming=game
    def player(self):
        return f"the name is {self.name} and game is {self.gaming}"
john=play('sriram','chess')
print(john.player())
#print(john._play__No_of_game)private key acess

class profile(play):
    pass
bala=profile("arjun","chess")
print(bala.player())
#print(bala.data())



class A:
    var="the Untold mystery of class A"
    def __init__(self):
        self.var1="continution"
        self.var="inside the fun A"
        self.spr="welcome"

class B(A):
    # var="the Untold mystery of class B"
    def __init__(self):
        super().__init__()
        self.var1="continution"
        self.var="inside the fun B"

a=A()
b=B()

print(b.var)


#int class
a=10
b=15
#print(a+b)
print(int.__add__(a,b))

class stu:  #operator Overloading
    def __init__(self,name,age,salary):
        self.Name=name
        self.Age=age
        self.Salary=salary

    def user(self):#any variable u can put
        return f"name is {self.Name} Age is {self.Age} and my salary is {self.Salary}"
    
    def __add__(self,other):
        return self.Salary+other.Salary
    def __sub__(self,other):
        return self.Salary-other.Salary
    def __mul__(self,other):
        return self.Salary*other.Salary

sri=stu('Srikanth',22,25000)
san=stu('Sanjai',21,20000)
print(sri.Salary+san.Salary)
print(sri+san)
print(sri-san)
print(sri*san)




#__str__, __repr__ Operator

a=10
a=int.__str__(a)
print(type(a))

class stu:  #operator Overloading
    def __init__(self,name,age,salary):
        self.Name=name
        self.Age=age
        self.Salary=salary

    def user(self):#any variable u can put
        return f"name is {self.Name} Age is {self.Age} and my salary is {self.Salary}"
    def __str__(self):
        return f"name is {self.Name} Age is {self.Age} and my salary is {self.Salary}"
    
    def __repr__(s):
        return f"Name is {s.Name} Age is {s.Age} and my Salary is {s.Salary}"
    
sri=stu('Srikanth',22,25000)
san=stu('Sanjai',21,20000)
print(san)
print(repr(sri))



#Abstract

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printvalue(self):
        return 0

class square(shape):
    type='square'
    sides=4

    def __init__(self):
        self.side=5

    def printvalue(self):
        return f"the area of square {self.side*self.side}"
    
s1=square()
print(s1.printvalue())


#  Setter   and property decorator

class Learner:
    def __init__(self,Program,database):
        self.mainprogram=Program
        self.databaselan=database
    @property
    def connect(self):
        if self.mainprogram==None or self.databaselan==None:
            return "The value in invalid"
        return f"{self.mainprogram}  {self.databaselan} developer"
    @connect.setter
    def connect(self,string):
        names=string.split("@")[0]
        self.mainprogram=names.split(".")[0]
        self.databaselan=names.split(".")[1]

    @connect.deleter
    def connect(self):
        self.mainprogram=None
        self.databaselan=None

    def learn(self):
        return f"The main language is {self.mainprogram} and database is {self.databaselan}"
    

s=Learner("python","Sql")
print(s.connect)#to run then function using property overloading
#print(s.connect())# to run the function
s.mainprogram="java"
print(s.connect)
print(s.learn())
s.connect="sri.25@gmail.com"
print(s.connect)

del s.connect
print(s.connect)


'''

#objectIntroSpection

class Learner:
    def __init__(self,Program,database):
        self.mainprogram=Program
        self.databaselan=database
    @property
    def connect(self):
        if self.mainprogram==None or self.databaselan==None:
            return "The value in invalid"
        return f"{self.mainprogram}  {self.databaselan} developer"
    @connect.setter
    def connect(self,string):
        names=string.split("@")[0]
        self.mainprogram=names.split(".")[0]
        self.databaselan=names.split(".")[1]

    @connect.deleter
    def connect(self):
        self.mainprogram=None
        self.databaselan=None

    def learn(self):
        return f"The main language is {self.mainprogram} and database is {self.databaselan}"
    
sri=Learner("program","database")
print(sri.connect)
print(id(sri))
print(dir(sri))

print(type("untoldmystery"))
print(id("untoldmystery"))


import inspect

print(inspect.getmembers)