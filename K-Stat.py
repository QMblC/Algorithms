from typing import List

def find_kth(array: List[int], k: int):

    left = []
    right = []
    middle = []

    if len(array) == 1:
        return array[0]
    
    pivot = array[-1]
     
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)

    length = len(left) + len(middle)

    if k < len(left):
        return find_kth(left, k)
    elif k < length:
        return middle[0]
    else:
        return find_kth(right, k - length)
    
array = [int(x) for x in input().split()]
k = int(input())

print(find_kth(array, k))
