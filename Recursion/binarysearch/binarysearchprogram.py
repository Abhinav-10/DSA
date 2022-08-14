def binary_search(arr, key):
    start,end = 0, len(arr)-1
    mid = (start+end)//2
    while start <= end:
        if arr[mid] == key:
            return f"{key} found at index {mid}"
        if key>arr[mid]:
            start=mid
        else:
            end=mid-1
    return f"{key} not Found in the given elements {arr}"

arr = [3,4,7,8,9,13,25,78]
print(binary_search(arr, 13))