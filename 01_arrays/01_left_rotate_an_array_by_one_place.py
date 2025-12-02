arr = [1,2,3,4,5]

# ans = [5,1,2,3,4]


ans = []
n = len(arr)

def approach1(arr):
    n = len(arr)
    for i in range(2 * n - 1):
        if i >= n - 1: ans.append(arr[i % n])
    return ans
    # S. C. -> O(n)
    # T. C. -> O(2 * n) ~ O(n)
    

def approach2(arr):
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp
    return arr
    # S. C. -> O(1)
    # T. C. -> O(n)


print(approach2(arr))