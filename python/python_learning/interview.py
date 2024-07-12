# Question: flatten the list

#  [[1,3, "raj"], [4,5], [6, [3,6,[1,2]]]]

# [[1,3, "raj"], [6, [88,89], [45, [46, 47]]], [4,5], [6, [3,6,[1,2]]]]


def flat_list(lst_data):
    lst = []
    for i in lst_data:
        if isinstance(i,list):
            lst.extend(flat_list(i))
        else:
            lst.append(i)
    return lst
    
# lst_data_1= [[1,3, "raj"], [4,5], [6, [3,6,[1,2]]]]
lst_data_1= [[1,3, "raj"], [6, [88,89], [45, [46, 47]]], [4,5], [6, [3,6,[1,2]]]]
lst = flat_list(lst_data_1)
print(lst)



# Given an integer array arr, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6. 

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


def sub_aaray(val):
    max_val = max_val_1= val[0]
    for i in val[1:]:
        max_val = max(i,max_val+ i)
        if max_val > max_val_1:
            max_val_1 = max_val
    return max_val_1
    
val_1 = [-2,1,-3,4,-1,2,1,-5,4]
var = sub_aaray(val_1)
print(var)
        
val_2 = [1]
var = sub_aaray(val_2)
print(var)

val_3 = [5,4,-1,7,8]
var = sub_aaray(val_3)
print(var)
