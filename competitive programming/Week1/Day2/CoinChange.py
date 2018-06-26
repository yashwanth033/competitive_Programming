def count(S, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1

    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]


if __name__ == '__main__':
    arr = eval(input("Enter list: "))
    n = int(input("Enter value: "))
    x = count(arr, len(arr), n)
    print(x)