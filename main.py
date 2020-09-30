import math


def jump_search(ys, el):
    length = len(ys)
    jump = int(math.sqrt(length))
    left = 0
    right = 0

    while left < length and ys[left] <= el:
        right = min(length - 1, left + jump)
        if ys[left] <= el and ys[right] >= el:
            break
        left += jump

    if left >= length or ys[left] > el:
        return -1

    right = min(length - 1, right)

    l = left
    while l <= right and ys[l] <= el:
        if ys[l] == el:
            return l
        l += 1
    return -1


arr = ['B', 'E', 'K', 'J', 'A', 'U', 'P']
data = 'E'


def letter_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if ord(arr[j]) > ord(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def letter_search(arr, data):
    arr = letter_sort(arr)
    ord_list = list(map(ord, arr))
    result = jump_search(ord_list, ord(data))
    print(result)


letter_search(arr, data)











