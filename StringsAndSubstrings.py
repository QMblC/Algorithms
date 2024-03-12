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

hash = [0]
powers = [1]

number = 1000000000003

for i in range(len(string)):
    hash.append(hash[i] * 26 + ord(string[i]) - 97)
    powers.append(powers[i] * 26)

find_min_k(hash, powers, string)