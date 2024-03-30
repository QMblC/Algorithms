array = input().split()

for i in range(len(array)):
    index = i
    for j in range(i + 1, len(array)):
        if int(array[j]) < int(array[index]):
            index = j
    value = array[i]
    array[i] = array[index]
    array[index] = value

    if i + 1 == len(array) // 2:
        print(" ".join(array))
print(" ".join(array))
