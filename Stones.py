stones = []

def count_pairs(i: int, j: int):
    if i >= stones_number:
        return 0
    
    if j >= stones_number:
        return count_pairs(i + 1, i + 2)

    if i < j and stones[i] >= stones[j]:
        return 1 + count_pairs(i, j + 1)
    else:
        return count_pairs(i, j + 1)

stones_number = int(input())

for i in range(stones_number):
    stones.append(int(input()))

a = count_pairs(0, 1)
print(a)