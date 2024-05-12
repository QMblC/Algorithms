array = [int(x) for x in input().split()]

for i in range(len(array)):

    value = array[i]
    index = i
    for j in range(index, 0, -1):
        if array[index - 1] > value:
            array[index] = array[index - 1]
            index -= 1
        else:
            break
    array[index] = value

    if i == (len(array) - 1) // 2:
       print(" ".join([str(x) for x in array]))

print(" ".join([str(x) for x in array]))