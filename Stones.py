def count_pairs(i):
    pairs = 0
    for j in range(i + 1, stones_number):
        if i < j and stones[i] >= stones[j]:
            pairs += 1
            pass
    return pairs

def sum_pairs(i = 0):
    if i == stones_number:
        return 0
    else:
        return count_pairs(i) + sum_pairs(i + 1)

def handle():
    for n in range(stones_number):
        stones.append(int(input()))


stones_number = int(input())
stones = []

handle()
print(sum_pairs())
