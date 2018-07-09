import random


def rand5():
    return random.randint(1, 5)


def random7():
    return 5 * rand5() + rand5() - 5


def rand7():
    while True:
        r = random7()
        if r < 22:
            return (r%7+1)


print('Rolling 7-sided die...')
print(rand7())