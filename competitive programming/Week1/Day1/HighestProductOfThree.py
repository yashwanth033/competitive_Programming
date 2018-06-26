def highest_product_of_3(input_ints):
    if len(input_ints) < 3:
        raise ValueError('Not enough numbers in list')

    high = max(input_ints[0], input_ints[1])
    low = min(input_ints[0], input_ints[1])
    hp_of_2 = input_ints[0] * input_ints[1]
    lp_of_2 = input_ints[0] * input_ints[1]
    hp_of_3 = input_ints[0] * input_ints[1] * input_ints[2]

    for i in range(2, len(input_ints)):

        hp_of_3 = max(hp_of_3, input_ints[i] * hp_of_2, input_ints[i] * lp_of_2)
        hp_of_2 = max(hp_of_2, input_ints[i] * high, input_ints[i] * low)
        lp_of_2 = min(lp_of_2, input_ints[i] * high, input_ints[i] * low)
        high = max(high, input_ints[i])
        low = min(low, input_ints[i])

    return hp_of_3

if __name__ == '__main__':
    testcase = eval(input())
    try:
        print(highest_product_of_3(testcase))
    except ValueError:
        print("Not enough numbers in list")