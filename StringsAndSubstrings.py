def find_min_k(hash, powers, string):
    max_sub_length = 0
    for sub_length in range(1, len(string)):
        if (len(string) % sub_length) != 0:
            continue
        for i in range(0, len(string) - sub_length * 2 + 1, sub_length):
            f_r = hash[i + sub_length] - hash[i] * powers[sub_length]
            s_r = hash[i + sub_length * 2] - hash[i + sub_length] * powers[sub_length]
            if f_r != s_r:
                continue
            max_sub_length = max(max_sub_length, sub_length)

    if (max_sub_length != 0):
        print(len(string) // max_sub_length, string[0: max_sub_length])
    else:
        print(1, string)

string = input() 

base = 26
alphabet = [chr(x) for x in range(97, 97 + base)]

hash = [0] * (len(string) + 1)
powers = [1] * (len(string) + 1)

number = 1000000000003

for i in range(len(string)):
    hash[i + 1] = hash[i] * base + alphabet.index(string[i])
    powers[i + 1] = powers[i] * base

print(hash)
print(powers)

find_min_k(hash, powers, string)