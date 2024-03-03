string = input()

n = len(string)
last_k = 0
last_substring = ""

for i in range(0, n):
    if i == 0:
        continue
    if n % i != 0:
        continue
    substring = string[0 : i]
    if substring * (n // i) == string:
        last_k = n // i
        last_substring = substring
        break

if (last_k == 0):
    last_k = 1
    last_substring = string

print(last_k, last_substring)