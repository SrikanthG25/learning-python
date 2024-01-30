'''

# os module

import os
# print(dir(os)) view inside os function
# print(os.getcwd())
# os.chdir("C:\\Users\Srikanth\Music")
# print(os.getcwd)
# f=open("file.txt") # to open file
# print(os.listdir("C:\\Users\Srikanth\Music")) # to view file da

# os.makedir() # to create file(to give file name inside the bracket)
#os.rename("old_name","new name")# to change file name
print(os.path.exists("sdfghjk"))#to check the path present or not


#to convert a data in binary form
import pickle
# car=["Audi","Benz","BMW"]
# file="cars.pkl"
# fileopen=open(file,"wb") #to open in binary code
# pickle.dump(car,fileopen)
# fileopen.close()

file="cars.pkl"
fileopen=open(file,"rb")
print(pickle.load(fileopen))# to open in teminal and its only run in sequence data

'''

#request module

import requests
r=requests.get("https://www.google.com/search?sca_esv=565345942&sxsrf=AM9HkKlcnBmbrtV4maI2B1eMrRPyajG1Vg:1694704437400&q=car&tbm=isch&source=lnms&sa=X&ved=2ahUKEwit4PX_saqBAxWprlYBHalyDFAQ0pQJegQIDRAB&biw=1920&bih=1001&dpr=1#imgrc=GL740lYp4YRWwM")
# print(r)
# print(r.content)
with open("redcar.jpg","wb") as f:
    f.write(r.content)