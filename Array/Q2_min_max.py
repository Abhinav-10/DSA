"""
Find the minimum and maximum element in an array using minimum comparisons

Input:  nums[] = [5, 7, 2, 4, 9, 6]
 
Output:
 
The minimum element is :: 2
The maximum element is :: 9

"""

nums = [5, 7, 2, 4, 9, 6]

minimum = maximum = nums[0]

for i in range(1, len(nums)):
    if nums[i]>maximum:
        maximum = nums[i]
    elif nums[i]<minimum:
        minimum = nums[i]
    
print(f"The minimum element is :: {minimum}")
print(f"The maximum element is :: {maximum}")


