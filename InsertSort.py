array = [int(x) for x in input().split()]

for i in range(len(array)):

    value = array[i]
    index = i
    while (index > 0) and (array[index - 1] > value):
        array[index] = array[index - 1]
        index -= 1
    array[index] = value

    print(array, i)

    #if i == len(array) // 2:
     #   print(" ".join([str(x) for x in array]))

print(" ".join([str(x) for x in array]))