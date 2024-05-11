from typing import List

k, m, n = [int(x) for x in input().split()]
array = [x for x in range(m, n + 1)]

def count(array: List[int], k, scores: List[int] = [], counter = 0):
    
    if len(scores) == k:

        print(" ".join(scores))
        return 1

    last_value = 999999999

    for i in array:

        if i < array[0] + k - 1 - len(scores):
            continue 

        if len(scores) != 0:
            last_value = int(scores[-1]) 

        if i < last_value:   
            new_scores = scores + [str(i)]
            counter += count(array, k, new_scores)
    
    return counter

counter = count(array, k)
print(counter)