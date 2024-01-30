'''
#__name__==__main__
def add(str):
    print(f"This is your string : {str}")

def mul(a,b):
    print(a*b)

print("The main fun : ",__name__)

if __name__=="__main__": # only inside the file should be run the function
    add("sri")
    mul(2,5)

'''

#function cache

import time
from functools import lru_cache
@lru_cache
# @lru_cache(maxsize=2) to taken last 2 variable only
def value(s):
    print("calculating")
    time.sleep(2)
    return s*100

if __name__=="__main__":
    var1=value(5)
    print(var1)
    var1=value(8)
    print(var1)
    var1=value(5)
    print(var1)