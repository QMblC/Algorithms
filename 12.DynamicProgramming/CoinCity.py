from typing import List

n, m = map(int, input().split())
tiles = []

for i in range(n):
    tiles.append([int(x) for x in input().split()])

def count_coins(n: int, m: int, tiles: List[int]):

    previous_row = [0] * m

    previous_row[0] = tiles[0][0]

    for j in range(1, m):
        previous_row[j] = previous_row[j - 1] + tiles[0][j]        
        
    for i in range(1, n):

        current_row = [0] * m
        current_row[0] = previous_row[0] + tiles[i][0]

        for j in range(1, m):
            current_row[j] = max(current_row[j - 1], previous_row[j]) + tiles[i][j]

        previous_row = current_row

    print(previous_row[-1])

count_coins(n, m, tiles)