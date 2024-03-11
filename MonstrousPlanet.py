def split_string(string: str):
    return [int(x) for x in string.split()]

def binary_search(first_type, second_type):
    left = 0
    right = l - 1

    while (right - left > 1):
        middle = (left + right) // 2
        if first_type[middle] <= second_type[middle]:
            left = middle
        else:
            right = middle

    if (max(first_type[left], second_type[left]) < max(first_type[right], second_type[right])):
        print(left)
    else:
        while right + 1 < l:
            if (first_type[right] == first_type[right + 1]):
                right += 1
            else:
                break
        print(right)

n, m, l = split_string(input())

first_type = [split_string(input()) for i in range(n)]
second_type = [split_string(input()) for i in range(m)]

q = int(input())
for i in range(q):
    request = split_string(input())
    binary_search(first_type[request[0]], second_type[request[1]])