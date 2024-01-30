'''
d={ "sri" : "B Tech ","san":"agri","sanjai":"B Com"}
print(d)
print(d["sri"])
d["rish"]="cse"
print(d)
del d["sanjai"]
print(d)
# d1=d
# del d1["san"]
# print(d1)
d1=d.copy()
del d1["san"]
d1.update({"yuva":"lusu"})
d1["a"]="paithiyam"
del d1["a"]
print(d1)
print(d1.values())
print(d1.keys( ))

'''

d={"sri":"B Tech IT","san":"Agri","rish":"cse"}
user=input("Enter the key : ")
print(d[user])