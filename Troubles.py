from typing import List

numbers = [int(x) for x in input().split()]

def quick_sort(array: list, left, right):
    if right - left <= 1:
        return array
    while right - left > 1:
        n = partition(array, left, right)
        if n - left > right - n:
            quick_sort(array, n, right)
            right = n
        else:
            quick_sort(array, left, n)
            left = n
            


def partition(array: List[int], left: int, right: int):
    if right - 1 <= left:
        return
    
    i = left
    j = right - 1

    pivot = array[-1]

    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        else:
            break

    return i

a = quick_sort(numbers, 0, len(numbers))
print(" ")
