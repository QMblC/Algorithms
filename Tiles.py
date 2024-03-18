n, m = [int(x) for x in input().split()]
tiles = [int(x) for x in input().split()]

middle = n // 2 + 1

result = []

base = 1000000
number = 1000000007

real_hash = [0]

pows = [1]

for i in range(n):
    real_hash.append((real_hash[i] * base + tiles[i]) % number)
    pows.append((pows[i] * base) % number)

for i in range(middle):
    first_hash = (real_hash[i] - real_hash[0] * pows[i]) % number
    second_hash = (real_hash[i * 2] - real_hash[i] * pows[i]) % number

    print(first_hash, second_hash)
    if str(first_hash) == str(second_hash)[::-1]:
        result.append(str(n - i))

print(" ".join(result))

