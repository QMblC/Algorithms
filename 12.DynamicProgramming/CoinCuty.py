n, m = [int(x) for x in input().split()]
tiles = []
for i in range(n):
    tiles.append([int(x) for x in input().split()])

def count_coins(n: int, m: int):

    current_tile_coins = tiles[n][m]

    if n == 0 and m == 0:
        return tiles[0][0]

    if n != 0:
        upper = count_coins(n - 1, m)
    else:
        return count_coins(n, m - 1) + tiles[n][m]
    
    if m != 0:
        left = count_coins(n, m - 1)
    else:
        return count_coins(n - 1, m) + tiles[n][m] 

    return max(left, upper) + tiles[n][m]

print(count_coins(n - 1, m - 1))