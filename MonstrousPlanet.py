import sys

n, m, l = [int(x) for x in input().split()]

first_type = [input().split() for x in range(n)]
second_type = [input().split() for x in range(m)]

q = int(input())


for x in range(q):

    request = input().split()

    left = 0
    right = l - 1

    while (right - left > 1):

        middle = (left + right) // 2

        if int(first_type[int(request[0])][middle]) <= int(second_type[int(request[1])][middle]):
            left = middle
        else:
            right = middle

    left_max = max(int(first_type[int(request[0])][left]), int(second_type[int(request[1])][left]))
    right_max = max(int(first_type[int(request[0])][right]), int(second_type[int(request[1])][right]))
    
    if (left_max < right_max):
        print(left)
    else:
        while True:
            if (right + 1 == l):
                break
            if (max(int(first_type[int(request[0])][right]), int(second_type[int(request[1])][right])) == \
                max(int(first_type[int(request[0])][right + 1]), int(second_type[int(request[1])][right + 1]))):
                right += 1
            else:
                break
        print(right)
