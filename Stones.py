def merge_sort(stones):
    if len(stones) == 1:
        return stones, 0
    
    left, p1 = merge_sort(stones[ : len(stones) // 2])
    right, p2 = merge_sort(stones[len(stones) // 2 : ])
    
    array, p = merge(left, right)
    
    return array, p + p1 + p2

def merge(left, right):
    array = []
    p = i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            p += len(left) - i
            array.append(right[j])
            j += 1
    
    array += left[i:] + right[j:]
    return array, p

stones = []
for n in range(int(input())):
    stones.append(int(input()))

a, p = merge_sort(stones)
print(p)