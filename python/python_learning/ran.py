import random 

p=random.randrange(1,10)
print(p)

p=random.randint()
print(p)
 
ran=random.random()
print(ran)
ran=random.random()*100
print(ran)

l=["sri","rish","krish","kumaran","vicky"]
r=random.choice(l)
print("Best name",r)

l=[25,31,25,14,2,19,21,15]
random.shuffle(l)
print(l)
