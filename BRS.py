from typing import List

k, m, n = [int(x) for x in input().split()]
array = [x for x in range(m, n + 1)]
counter = 0

def count(array: List[int], k, scores: List[int] = []):
    
    if len(scores) == k:
        global counter
        counter += 1
        print(" ".join(scores))
        return

    last_value = 999999999

    for i in array:

        if i < array[0] + k - 1 - len(scores):
            continue 

        if len(scores) != 0:
            last_value = int(scores[-1]) 

        if i < last_value:   
            new_scores = scores + [str(i)]
            count(array, k, new_scores)

count(array, k)
print(counter)