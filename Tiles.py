n, m = [int(x) for x in input().split()]
tiles = [int(x) for x in input().split()]

middle = n // 2
if n % 2 == 0:
    middle += 1

real_hash = [0]
reversed_hash = [0]

for i in range(n):
    real_hash.append(real_hash[i] * 1000000 + tiles[i])
    reversed_hash.append(reversed_hash[i] * 1000000 + tiles[n - 1 - i])

print(real_hash)
print(reversed_hash)


print()

print(real_hash[3])