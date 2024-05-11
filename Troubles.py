from typing import List

def quick_sort(array: List[int], left: int, right: int):

    if left >= right:
        return
    
    pivot = partition(array, left, right, array[right])

    print(array[pivot])

    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)

def partition(array: List[int], left: int, right: int, pivot: int):
    
    i = left
    j = right

    while i <= j:

        while array[i] < pivot:
            i += 1

        while i <= j and array[j] >= pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[i], array[right] = array[right], array[i]

    return i


array = [int(x) for x in input().split()]

quick_sort(array, 0, len(array) - 1)
print(" ".join([str(x) for x in array]))