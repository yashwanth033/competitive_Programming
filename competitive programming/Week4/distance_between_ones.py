n = int(input())
result = 0
count = 1
flag = False
negative = False
if n < 0:
    negative = True
    n = abs(n)
while n != 0:
    if n % 2 == 1:
        if flag is True:
            if result < count:
                result = count
                count = 1
        flag = True
    elif flag is True:
        count += 1
    n = n >> 1
if negative:
    if 1 > result:
        result = 1
print(result)
