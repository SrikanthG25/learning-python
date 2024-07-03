# def add(a,b):
#     return a+b
# print(add(10,15))


# a=lambda a,b:a+b
# print(a(10,1))

# def product_except_self(nums):
#     length = len(nums)
#     answer = [0] * length

#     left_product = 1
#     for i in range(length):
#         answer[i] = left_product
#         left_product *= nums[i]

#     right_product = 1
#     for i in range(length - 1, -1, -1):
#         answer[i] *= right_product
#         right_product *= nums[i]

#     return answer

# input_list = [1, 2, 3, 4]
# output_list = product_except_self(input_list)
# print(output_list)

# class ProductArray:
#     def __init__(self, nums):
#         self.nums = nums

#     def product_except_self(self):
#         length = len(self.nums)
#         answer = [0] * length

#         left_product = 1
#         for i in range(length):
#             answer[i] = left_product
#             left_product *= self.nums[i]

#         right_product = 1
#         for i in range(length - 1, -1, -1):
#             answer[i] *= right_product
#             right_product *= self.nums[i]

#         return answer

# input_list = [1, 2, 3, 4]
# product_array = ProductArray(input_list)
# output_list = product_array.product_except_self()
# print(output_list)




i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i += 1


p = "Am having knowledge with real time project , in python , django, restframework,API development,manual and unit testing, gitlab, Github , jira ,  mysql , postman APIs , Dbeaver.To developing an projects like Jira ticketing tool in my internship periods and gain more knowledge in real time work environment , leaning  in ML to develop the projects in basically"
print(len(p))

v ="Am having knowledge with real time project , in python , Django, restframework,API development,manual and unit testing, gitlab, Github , jira ,  mysql , postman APIs , Dbeaver."
print(len(v))