import sys

def find_position(arr_legs, arr_hands, ids, l):
    for id in ids:
        legs = arr_legs[int(id[0])]
        hands = arr_hands[int(id[1])]
        arr_max = [max(int(legs[i]), int(hands[i])) for i in range(l)]
        min_limbs = sys.maxsize
        min_index = 0
        for i in range(l - 1, -1, -1):
            if arr_max[i] < min_limbs:
                min_limbs == arr_max[i]
                print(i)
                break

info = input().split()
arr_legs = [input().split() for i in range(int(info[0]))]
arr_hands = [input().split() for i in range(int(info[1]))]

q = int(input())
ids = [input().split() for i in range(q)]
for id in ids:
        legs = arr_legs[int(id[0])]
        hands = arr_hands[int(id[1])]
        arr_max = [max(int(legs[i]), int(hands[i])) for i in range(int(info[2]))]
        min_limbs = sys.maxsize
        min_index = 0
        for i in range(int(info[2]) - 1, -1, -1):
            if arr_max[i] < min_limbs:
                min_limbs = arr_max[i]
                min_index = i
            elif arr_max[i] == min_limbs:
                 continue
            else:
                 break
        print(min_index)