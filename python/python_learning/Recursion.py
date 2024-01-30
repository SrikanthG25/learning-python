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
