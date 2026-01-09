# Time complexity: O(n)

def kadane(arr):
    currSum = maxSum = arr[0]

    for i in range(len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)

    return maxSum