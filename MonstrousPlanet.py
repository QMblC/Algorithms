import sys

n, m, l = [int(x) for x in input().split()]

first_type = [input().split() for x in range(n)]
second_type = [input().split() for x in range(m)]

q = int(input())

completed = dict()
result = []

for x in range(q):

    request = input().split()

    if (request[0] + " " + request[1]) in completed:
        result.append(completed[request[0] + " " + request[1]])
        continue

    last_value = sys.maxsize
    last_index = 0

    for index in range(l):

        max_element = max(int(first_type[int(request[0])][index]), int(second_type[int(request[1])][index]))
        if (last_value >= max_element):
            last_value = max_element
            last_index = index
        else: 
            break

    completed[request[0] + " " + request[1]] = last_index
    result.append(str(last_index))
print("\n".join(result))
