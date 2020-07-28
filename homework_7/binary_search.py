def binary_search(number, array):
    if len(array) == 1:
        if array[0] == number:
            return number
        else:
            return "No"
    array.sort()
    mid_number_index = len(array) // 2
    if number > array[mid_number_index]:
        return binary_search(number, array[mid_number_index + 1:])
    elif number < array[mid_number_index]:
        return binary_search(number, array[:mid_number_index])
    else:
        return number


number = int(input())
array = [16, 9, 24, 35, 30, 500, 0, 1, 91, 45, 78]
print(binary_search(number, array))
