numbers = [int(x) for x in input().split()]
k = int(input())

def get_kth(array: list, k: int):
    l = 0
    r = len(array)

    while l + 1 < r:
        m = separate(array,l,r)
        if k >= m:
            l = m
        else:
            r = m
        return array[l]


def separate(array: list, left, right):
    if right - left < 1:
        return left
    i = left
    j = right - 1

    pivot = array[0]

    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
            j -= 1
        else:
            break
    return i

array = get_kth(numbers, k)
print(array)
