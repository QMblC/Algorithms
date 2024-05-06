numbers = [int(x) for x in input().split()]

def quick_sort(array: list):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop(-1)       
        left, right = separate(array, pivot)
        stage = quick_sort(left) + [pivot] + quick_sort(right)
        
        return stage

def separate(array: list, pivot: int):
    left = []
    right = []
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return left, right

print(quick_sort(numbers))