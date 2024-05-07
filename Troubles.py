numbers = [int(x) for x in input().split()]

def quick_sort(array: list):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop(-1)       
        left, right = separate(array, pivot)
        a = quick_sort(left)
        b = quick_sort(right)
        stage = a + [pivot] + b
        print(a, pivot, b)
        print(stage, end="\n\n")
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

a = quick_sort(numbers)
print(" ".join([str(x) for x in a]))
