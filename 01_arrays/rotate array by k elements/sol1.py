arr = [1,2,3,4,5,6,7]
k = 2

# ans = [6,7,1,2,3,4,5]

ans = []
n = len(arr)
for i in range(2 * n - (k + 1)):
    if i >= n - k: ans.append(arr[i % n])

print(ans)

# S. C. -> O(n)
# T. C. -> O(2 * n) ~ O(n)