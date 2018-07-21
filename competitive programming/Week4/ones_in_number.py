def ones(x):
    count = 0
    while x != 0:
        if x%2 == 1:
            count += 1
        x = x >> 1
    return count


n = int(input())
result = []
for i in range(n+1):
    result.append(ones(i))
print(result)