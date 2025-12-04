from collections import Counter


arr = [2,1,2,4,1]

# ans = 4

n = len(arr)
def approach1(arr):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                
        if count == 1: return arr[i]
    # S. C. -> O(1)
    # T. C. -> O(n ^ 2)
    

def approach2a(arr):
    counter = Counter(arr)
    for key, value in counter.items():
        if value == 1:
            return key

def approach2b(arr):
    freq = {}
    for i in range(n):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    for key, value in freq.items():
        if value == 1:
            return key

    # For both 2a and 2b:
        # S. C. -> O(n/2) ~ O(n)
        # T. C. -> O(n + n/2) ~ O(n)

def approach3(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
    return xor
    # S. C. -> O(1)
    # T. C. -> O(n)

print(approach3(arr))