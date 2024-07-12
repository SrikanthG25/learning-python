# a=1
# while a<=5:
#     print("Untold",end=" ")
#     b=1
#     while b<=1:
#         print("Mystery",end=" ")
#         b+=1
#     a=a+1
#     print()
# #nested if statement
# a=45
# if a>10:
#     print("above 10")
#     if a>20:
#         print("above twenty")
#     else:
#         print("Error")


# def add(a,b):
#     return a+b
# print(add(20,5))
# # args --- > tuple value
# def add(*args):
#     return sum(args)
# print(add(20,5))



def find_second_largest(*args):
    arr = sorted(set(args), reverse=True)
    return arr[1] if len(arr) > 1 else None

lst = [3, 1, 51, 17, 45, 2]
result = find_second_largest(*lst)
print(f"The second largest number in the array is: {result}")