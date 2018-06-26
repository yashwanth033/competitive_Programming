def get_products_of_others(input_list):
    if len(input_list) < 2:
        raise IndexError('Error Less than two numbers')

    result = [None] * len(input_list)
    product = 1

    for i in range(len(input_list)):
        result[i] = product
        product *= input_list[i]

    product = 1

    for i in range((len(input_list) - 1), -1, -1):
        result[i] *= product
        product *= input_list[i]

    return result

if __name__ == '__main__':
    input = eval(input())

    try:
        print(str(get_products_of_others(input)))
    except IndexError:
        print("Error Less than two numbers")