'''
#function call in inside the fun
def august():
    print("The August in middle of the year")
    august()
august()

'''

def fat(a):
    if a==0:
        return 1
    return a*fat(a-1)
res=fat(5)
print(res)


# import re

# text = '''
# {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
# '''

# pattern = r'\b\d+\b'

# numbers = re.findall(pattern, text)

# numbers = list(map(int, numbers))

# print(numbers)

# a ={1,2,3}
# b ={3,4,5}
# print(a&b)
