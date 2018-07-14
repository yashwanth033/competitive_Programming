def hamming(x, y):
    count = 0
    while (y != x):
        if (y % 2 != x % 2):
            count += 1
        x = x // 2
        y = y // 2
    return count


if __name__ == "__main__":
    print(hamming(25, 30))
    print(hamming(1,4))
    print(hamming(25,30))
    print(hamming(100,250))
    print(hamming(1,30))
    print(hamming(0,255))
