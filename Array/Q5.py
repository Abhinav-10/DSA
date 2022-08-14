"""
WAP to Move all negative numbers to beginning and positive to end with constant extra space

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

"""
# sol 1:
nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

# positive = []
# negative = []

# for num in nums:
#     if num<0:
#         negative.append(num)
#     else:
#         positive.append(num)
        
# negative.extend(positive)  
# print(negative)

# sol 2

nums.sort()

for num in nums:
    print(num , end = ' ')