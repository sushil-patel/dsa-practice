arr = [1,2,3,4,5,6,7]
k = 2

# ans = [6,7,1,2,3,4,5]

ans = []
n = len(arr)
def approach1(arr):
    for i in range(2 * n - k):
        if i >= n - k: ans.append(arr[i % n])
    return ans
    # S. C. -> O(n)
    # T. C. -> O(2n) ~ O(n)


def approach2(arr):
    last_k_ele = []
    for i in range(n - k, n):
        last_k_ele.append(arr[i])

    for i in range(n - 1, -1, -1):
        if i >= k: arr[i] = arr[i - k]
        else: arr[i] = last_k_ele[i]
    return arr
    # S. C. -> O(k)
    # T. C. -> O(2k * (n - k)) ~ O(n)


def approach3(arr):
    def reverse(arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    return arr
    # S. C. -> O(1)
    # T. C. -> O(2n) ~ O(n)


print(approach3(arr))

