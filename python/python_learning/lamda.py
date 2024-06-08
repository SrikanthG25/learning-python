# def add(a,b):
#     return a+b
# print(add(10,15))


# a=lambda a,b:a+b
# print(a(10,1))

def product_except_self(nums):
    length = len(nums)
    answer = [0] * length

    left_product = 1
    for i in range(length):
        answer[i] = left_product
        print(answer[i])
        left_product *= nums[i]

    right_product = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= right_product
        print(answer[i])
        right_product *= nums[i]

    return answer

input_list = [1, 2, 3, 4]
output_list = product_except_self(input_list)
# print(ou tput_list)

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