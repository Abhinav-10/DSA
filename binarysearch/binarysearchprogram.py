def binary_search(arr, key):
    start,end = 0, len(arr)-1
    print(start, end)
    while start <= end:
        mid = (start+end)//2 # wouldn't work for long integers so use  mid = start+(end-start)//2
        if arr[mid] == key:
            return f"{key} found at index {mid}"

        # taking the right part
        elif key>arr[mid]:
            start=mid+1
        # taking the left part
        else:
            end=mid-1
    # if key does not exist
    return f"{key} not Found in the given elements {arr}"

arr = [10, 20, 30, 50, 80, 110, 130, 140, 170]
print(binary_search(arr,20))
