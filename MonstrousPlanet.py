import sys

n, m, l = [int(x) for x in input().split()]

first_type = [input().split() for x in range(n)]
second_type = [input().split() for x in range(m)]

q = int(input())


"""
def get_test_values():
    pass
n, m, l = 4, 3, 5
first_type = [[],[],[],[]]
first_type[0] = [1, 2, 3, 4, 5]
first_type[1] = [1, 1, 1, 1, 1]
first_type[2] = [0, 99999, 99999, 99999, 99999]
first_type[3] = [0, 0, 0, 0, 99999]
second_type = [[],[],[]]
second_type[0] = [5, 4, 3, 2, 1]
second_type[1] = [99999, 99999, 99999, 0, 0]
second_type[2] = [99999, 99999, 0, 0, 0]
q = 12
requests = [[],[],[],[],[],[],[],[],[],[],[],[]]
requests[0] = [0, 0]
requests[1] = [0, 1]
requests[2] = [0, 2]
requests[3] = [1, 0]
requests[4] = [1, 1]
requests[5] = [1, 2]
requests[6] = [2, 0]
requests[7] = [2, 1]
requests[8] = [2, 2]
requests[9] = [3, 0]
requests[10] = [3, 1]
requests[11] = [3, 2]
"""

completed = dict()

for x in range(q):

    request = input().split()

    if (request[0] + " " + request[1]) in completed:
        print(completed[request[0] + " " + request[1]])
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
    print(last_index)
