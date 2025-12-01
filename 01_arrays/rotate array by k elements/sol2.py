arr = [1,2,3,4,5,6,7]
k = 2

# ans = [6,7,1,2,3,4,5]

n = len(arr)
last_k_ele = []
for i in range(n - k, n):
    last_k_ele.append(arr[i])

# print(last_k_ele)

for i in range(n - 1, -1, -1):
    arr[i] = arr[i - k] if i >= k else last_k_ele[i]
    # if i >= k: arr[i] = arr[i - k]
    # else: arr[i] = last_k_ele[i]

print(arr)

# S. C. -> O(k)
# T. C. -> O(2k * (n - k)) ~ O(n)