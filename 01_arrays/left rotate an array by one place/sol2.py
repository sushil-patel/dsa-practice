arr = [1,2,3,4,5]

# ans = [5,1,2,3,4]

arr.insert(0, arr.pop())

print(arr)

# S. C. -> O(1)
# T. C. -> O(n) as the insertion would require shifting of all (n - 1) elements