array = [int(x) for x in input().split()]

for i in range(len(array)):
    index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[index]:
            index = j
    array[i], array[index] = array[index], array[i]

    if i + 1 == len(array) // 2:
        print(*array, sep= " ")

print(*array, sep= " ")