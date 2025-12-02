arr = [0,1,0,3,12]

# ans = [1, 2, 3, 4, 1, 0, 0, 0]


def appraoch(arr):
    p_0 = -1
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            p_0 = i
            break

    if p_0 == -1: return arr

    for i in range(p_0 + 1, n):
        if arr[i] != 0:
            arr[i], arr[p_0] = arr[p_0], arr[i]
            p_0 += 1
    return arr


print(appraoch(arr))

# S. C. -> O(1)
# T. C. -> O(n)