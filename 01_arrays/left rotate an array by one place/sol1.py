arr = [1,2,3,4,5]

# ans = [5,1,2,3,4]

ans = []
n = len(arr)
for i in range(2 * n - 1):
    if i >= n - 1: ans.append(arr[i % n])

print(ans)

# S. C. -> O(n)
# T. C. -> O(2 * n) ~ O(n)