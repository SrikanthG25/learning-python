def ser_data(arr , key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1
arr_size = int(input())
arr = []
for i in range(arr_size):
    num = int(input())
    arr.append(num)
key = int(input())
result= ser_data(arr , key)
if result != -1:
    print("SUCCESSFUL")
else:
    print("UNSUCCESSFUL")
