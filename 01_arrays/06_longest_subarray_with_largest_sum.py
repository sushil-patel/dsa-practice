arr = [10, 5, 2, 7, 1, 9]
k = 15

n = len(arr)

def reset_limits(j):
    sum_ = 0
    limit = j


def approach1_v1(arr, k):        
    max_length = 0
    for i in range(n):
        sum_ = arr[i]
        for j in range(i + 1, n):
            limit = i
            sum_ += arr[j]
            if sum_ > k:
                reset_limits()
            elif sum_ == k:
                reset_limits()
                max_length = max(max_length, j - limit + 1)
    return max_length
    # S. C. -> O(1)
    # T. C. -> O(n ^ 2)


def approach1_v2(arr, k):        
    max_length = 0
    ans = []
    for i in range(n):
        sum_ = arr[i]
        for j in range(i + 1, n):
            limit = i
            sum_ += arr[j]
            if sum_ > k:
                reset_limits(j)
            elif sum_ == k:
                reset_limits(j)
                current_length = j - limit + 1
                if current_length > max_length:
                    max_length = current_length
                    ans = arr[limit:j+1]
    return ans
    # S. C. -> O(n)
    # T. C. -> O(n ^ 2)


def approach2_v1(arr, k):
    sum_ = 0
    len = 0
    mpp = {}
    for i in range(n):
        sum_ += arr[i]
        if sum_ not in mpp:
            mpp[sum_] = i
        if sum_ == k:
            len = max(len, i + 1)
        rem = sum_ - k
        if rem in mpp:
            len = max(len, i - mpp[rem])
    return len
    # S. C. -> O(n)
    # T. C. -> O(n)


def approach2_v2(arr, k):
    sum_ = 0
    max_len = len = 0
    mpp = {}
    ans = []
    for i in range(n):
        sum_ += arr[i]
        if sum_ not in mpp:
            mpp[sum_] = i
        if sum_ == k:
            len = i + 1
            if len > max_len:
                ans = arr[ : i+1]
        rem = sum_ - k
        if rem in mpp:
            len = i - mpp[rem]
            if len > max_len:
                ans = arr[mpp[rem] + 1 : i + 1]
    return ans
    # S. C. -> O(n) + O(n) ~ O(n)
    # T. C. -> O(n)


# approach 3 is only for negative numbers

def approach3_v1(arr, k):
    sum_ = 0
    left = right = 0
    len = 0
    while right < n:
        while sum_ > k and left <= right:
            left += 1
            sum_ -= arr[left]
        if sum_ == k:
            len = max(len, right - left)
        right += 1
        if right < n: sum_ += arr[right]
    return len
    # S. C. -> O(1)
    # T. C. -> O(n) + O(n) ~ O(n)


def approach3_v2(arr, k):
    sum_ = 0
    left = right = 0
    length = max_length = 0
    ans = []
    while right < n:
        while sum_ > k and left <= right:
            left += 1
            sum_ -= arr[left]
        if sum_ == k:
            length = right - left
            if length > max_length:
                max_length = length
                ans = arr[left + 1: right + 1]
        right += 1
        if right < n: sum_ += arr[right]
    return ans
    # S. C. -> O(n)
    # T. C. -> O(n) + O(n) ~ O(n)


print(approach3_v2(arr, k))