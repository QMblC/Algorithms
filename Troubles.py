from typing import List

def quick_sort(array: List[int], left: int, right: int):

    if left >= right:
        return
    
    pivot_index = partition(array, left, right, array[right])

    print(array[pivot_index])

    quick_sort(array, left, pivot_index - 1)
    quick_sort(array, pivot_index + 1, right)

def partition(array: List[int], left: int, right: int, pivot: int):

    i = left
    j = right

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] >= pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]

    array[i], array[right] = array[right], array[i]

    return i

arr = [179, 181, 165, 184, 190, 152, 167]
quick_sort(arr, 0, len(arr) - 1)
print(arr)