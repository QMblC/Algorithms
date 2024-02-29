from functools import lru_cache

n, m, l = [int(x) for x in input().split()]

ft = [input() for x in range(n)]
st = [input() for x in range(m)]

q = int(input())

@lru_cache
def split_string(string: str):
    print(f"I'm in with {string}")
    return string.split()


for x in range(q):

    request = input().split()

    left = 0
    right = l - 1

    first_type = split_string(ft[int(request[0])])
    second_type = split_string(st[int(request[1])])

    while (right - left > 1):

        middle = (left + right) // 2

        if int(first_type[middle]) <= int(second_type[middle]):
            left = middle
        else:
            right = middle

    if (max(int(first_type[left]), int(second_type[left])) < max(int(first_type[right]), int(second_type[right]))):
        print(left)
    else:
        while right + 1 < l:
            
            if (max(int(first_type[right]), int(second_type[right])) == \
                max(int(first_type[right + 1]), int(second_type[right + 1]))):
                right += 1
            else:
                break
            
        print(right)
