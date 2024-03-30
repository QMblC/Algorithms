array = [int(x) for x in input().split()]
k = int(input())

is_printed = False

for i in range(len(array)):
    for j in range(len(array) - 1 - i):
        if (array[j] > array[j + 1]):
            value = array[j]
            array[j] = array[j + 1]
            array[j + 1] = value
    
    if (i + 1) % k == 0 and not(is_printed):
        print(" ".join([str(x) for x in array]))
        is_printed = True
        continue
    elif (i + 1) == len(array):
        print(" ".join([str(x) for x in array]))
        continue