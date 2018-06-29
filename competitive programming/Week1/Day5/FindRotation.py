def FindRotate(arr, low, high):
    if high < low:
        return 0

    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid + 1] < arr[mid]:
        return mid + 1

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid

    if arr[high] > arr[mid]:
        return FindRotate(arr, low, mid - 1)
    return FindRotate(arr, mid + 1, high)

if __name__ == '__main__':
    arr = ['ptolemaic', 'retrograde', 'supplant','undulate', 'xenoepist', 'asymptote','babka', 'banoffee', 'engender','karpatka', 'othellolagkage']
    high = len(arr)-1
    print(FindRotate(arr,0,high))