numbers = [int(x) for x in input().split()]
k = int(input())

def get_kth(array: list, k: int):
    l = 0
    r = len(array)

    while l + 1 < r:
        m = partition(array,l,r)
        if k >= m:
            l = m
        else:
            r = m
        return array[l]


def partition(array, left: int, right: int):
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

array = get_kth(numbers, k)
print(array)
