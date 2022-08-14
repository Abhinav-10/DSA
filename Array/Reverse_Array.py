"""
Write a program to reverse an array or string

Examples : 
 
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""

array_to_reverse = [1, 2, 3, 4, 5, 6]

print("Original Array", array_to_reverse)
start = 0
end = len(array_to_reverse)-1

while start < end:
    array_to_reverse[start], array_to_reverse[end] = array_to_reverse[end], array_to_reverse[start]
    start += 1
    end -= 1

print("Reversed Array", array_to_reverse)