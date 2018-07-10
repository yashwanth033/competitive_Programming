def print_repeating(arr):

    for i in range(0,len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])

if __name__ == '__main__':
    print(print_repeating([1, 1]))
    print(print_repeating([1, 2, 3, 2]))
    print(print_repeating([1, 2, 5, 5, 5, 5]))
    print(print_repeating([4, 1, 4, 8, 3, 2, 7, 6, 5]))