first_array = [int(x) for x in input().split()]
second_array = [int(x) for x in input().split()]

counter = dict()

for item in second_array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

for index, item in enumerate(first_array):
    if index == len(first_array) - 1:
        ending = ""
    else:
        ending = " "

    if item in counter:
        print(counter[item], end = ending)
    else:
        print(0, end = ending)