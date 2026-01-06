# Time complexity: O(log n)
# NOTE: Works on sorted arrays only!

def binary_search(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        
        if arr[middle] > target: end = middle - 1
        elif arr[middle] < target: start = middle + 1
        else: return middle

    return -1