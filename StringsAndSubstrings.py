def find_min_k(hash, string):

    max_sub_length = 0

    for sub_length in range(1, len(string)):

        flag = False
        if (len(string) % sub_length) != 0:
            continue

        for i in range(0, len(string) - sub_length * 2 + 1, sub_length):
            first_hash = hash[i + sub_length] - hash[i] * pows[sub_length]
            second_hash = hash[i + sub_length * 2] - hash[i + sub_length] * pows[sub_length]

            if first_hash != second_hash:
                flag = True
                break
        if flag:
            continue
        else:
            max_sub_length = max(max_sub_length, sub_length)
            break
        
    if (max_sub_length != 0):
        print(len(string) // max_sub_length, string[0: max_sub_length])
    else:
        print(1, string)

string = input() 

hash = [0]
pows = [1]

for i in range(len(string)):
    hash.append(hash[i] * 26 + ord(string[i]) - 97)
    pows.append(pows[i] * 26)

find_min_k(hash, string)
