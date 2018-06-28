def binarySearch(arr, l, h, x):
    while l <= h:
        mid = l + (h - l) // 2;
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            h = mid - 1
    return False

def contains(ordered_list, number):
    result = binarySearch(ordered_list, 0, (len(ordered_list) - 1), number)
    return result

if __name__ == '__main__':
    print(contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))