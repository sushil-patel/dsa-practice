arr = [1, 0, 2, 3, 0, 4, 0, 1]

# ans = [1, 2, 3, 4, 1, 0, 0, 0]


def approach1(arr):
    count_of_0 = 0
    ans = []
    n = len(arr)
    for i in arr:
        if i != 0: ans.append(i)
        else: count_of_0 += 1

    while count_of_0 > 0:
        ans.append(0)
        count_of_0 -= 1
    return ans
    # S. C. -> O(n)
    # T. C. -> O(n)


def approach2(arr):
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
    # S. C. -> O(1)
    # T. C. -> O(n)


print(approach2(arr))
