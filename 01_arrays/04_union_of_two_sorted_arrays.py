arr1 = [1,2,3,4,4,5]
arr2 = [3,4,6,7]

# ans = [1,2,3,4,5,6,7]

n1 = len(arr1)
n2 = len(arr2)
ans = []


def approach1(arr1, arr2):
    freq = {}
    for i in range(n1):
        freq[arr1[i]] = freq.get(arr1[i], 0) + 1
    for j in range(n2):
        freq[arr2[j]] = freq.get(arr2[j], 0) + 1
    l = sorted(freq)
    print(f'l which is a {type(l)} = {l}')
    
    return l
    # S. C. -> O(n1 + n2) ~ O(n)
    # T. C. -> O(n1 + n2) * log(n1 + n2) ~ O(n logn)


def approach2(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return sorted(set1 | set2) # union of set
    # return sorted(set1.union(set2))
    # S. C. -> O(n1 + n2) ~ O(n)
    # T. C. -> O((n1 + n2) * log(n1 + n2)) ~ O(n logn)


def approach3(arr1, arr2):
    p1 = p2 = 0
    while p1 < n1 and p2 < n2:
        if arr1[p1] < arr2[p2]:
            if not ans or ans[-1] != arr1[p1]: ans.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            if not ans or ans[-1] != arr2[p2]: ans.append(arr2[p2])
            p2 += 1
        else:
            if not ans or ans[-1] != arr1[p1]: ans.append(arr1[p1])
            p1 += 1
            p2 += 1
    
    while p1 < n1:
        if not ans or ans[-1] != arr1[p1]: ans.append(arr1[p1])
        p1 += 1
    while p2 < n2:
        if not ans or ans[-1] != arr2[p2]: ans.append(arr2[p2])
        p2 += 1
    return ans
    # S. C. -> O(n1 + n2) ~ O(n)
    # T. C. -> O(n1 + n2) ~ O(n)


print(approach3(arr1, arr2))