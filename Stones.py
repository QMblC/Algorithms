def count_pairs(i, j):
    if j == stones_number:
        return 0
    elif stones[i] >= stones[j]:
        return 1 + count_pairs(i, j + 1)
    else:
        return count_pairs(i, j + 1)

def sum_pairs(i = 0):
    if i == stones_number:
        return 0
    else:
        return count_pairs(i, i + 1) + sum_pairs(i + 1)

def handle():
    for i in range(stones_number):
        stones.append(int(input()))

stones_number = int(input())
stones = []

handle()
print(sum_pairs())
