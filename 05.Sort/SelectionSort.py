def select_sort(array):
    for i in range(length):
        index = i
        for j in range(i + 1, length):
            if array[j] < array[index]:
                index = j
        array[i], array[index] = array[index], array[i]

        if i + 1 == middle:
            print(" ".join(str(x) for x in array))

    return array

array = [int(x) for x in input().split()]
length = len(array)
middle = length // 2

print(" ".join(str(x) for x in select_sort(array)))