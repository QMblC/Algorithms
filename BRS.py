from typing import List

k, m, n = [int(x) for x in input().split()]
counter = 0

def count(min: int, max: int , k, scores: List[int]):
    
    if len(scores) == k:
        global counter
        counter += 1
        print(" ".join(scores))
        return

    last_value = 999999999

    for i in range(min, max):
        if len(scores) != 0:
            last_value = int(scores[-1])
        else:
            if i < min + k - 1:
                continue   

        if i < last_value:   
            new_scores = scores + [str(i)]
            count(min, max, k, new_scores)

count(m, n + 1, k, [])
print(counter)