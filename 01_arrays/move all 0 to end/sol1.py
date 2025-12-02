arr = [0,1,0,3,12]

# ans = [1,3,12,0,0]

count_of_0 = 0
ans = []
n = len(arr)
for i in arr:
    if i != 0: ans.append(i)
    else: count_of_0 += 1

while count_of_0 > 0:
    ans.append(0)
    count_of_0 -= 1

print(ans)

# S. C. -> O(n)
# T. C. -> O(n)