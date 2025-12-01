arr = [1,2,3,4,5,6,7]
k = 2

# ans = [6,7,1,2,3,4,5]

n = len(arr)
def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

reverse(arr, 0, n - 1)
reverse(arr, 0, k - 1)
reverse(arr, k, n - 1)
print(arr)

# S. C. -> O(1)
# T. C. -> O(2n) ~ O(n)