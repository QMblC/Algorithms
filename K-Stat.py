from typing import List

def partition(array: List[int], left: int, right: int):

    pivot = array[right]
    i = left
    j = left

    while j < right:

        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1

    array[i], array[right] = array[right], array[i]

    return i

def find_kth(array: List[int], left: int, right: int, k: int):

    if left <= right:
        pivot_index = partition(array, left, right)
        if pivot_index == k:
            print(array[pivot_index])
            return
        elif pivot_index < k:
            find_kth(array, pivot_index + 1, right, k)
        else:
            find_kth(array, left, pivot_index - 1, k)
    
array = [int(x) for x in input().split()]

k = int(input())

find_kth(array, 0, len(array) - 1, k)
