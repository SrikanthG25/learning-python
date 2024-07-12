def ser_data(arr , key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return 0
arr_size = int(input("Enter value : "))
arr = []
for i in range(arr_size):
    num = int(input("value : "))
    arr.append(num)
key = int(input("search :"))
result= ser_data(arr , key)
if result != 0:
    print("SUCCESSFUL")
else:
    print("UNSUCCESSFUL")
