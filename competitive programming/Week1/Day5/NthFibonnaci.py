def fib(n):
    a = 0
    b = 1
    if n < 0:
        raise ValueError("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

if __name__ == '__main__':
    print(fib(-1))