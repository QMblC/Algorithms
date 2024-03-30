array = input().split()

for i in range(len(array)):
    index = i
    for j in range(i + 1, len(array)):
        if int(array[j]) < int(array[index]):
            index = j
    array[i], array[index] = array[index], array[i]

    if i + 1 == len(array) // 2:
        print(" ".join(array))
print(" ".join(array))
