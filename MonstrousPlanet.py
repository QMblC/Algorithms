def split_string(string: str):
    splitted_array = []
    number = 0
    count = 0
    for char in string:
        
        if char == ' ':
            splitted_array.append(int(round(number * 10 ** (count - 1))))
            number = 0
            count = 0
        else:
            number += int(char) * 0.1 ** count
            count += 1
            
    splitted_array.append(int(round(number * 10 ** (count - 1))))
    return splitted_array

def binary_search(first_type, second_type):
    left = 0
    right = l - 1

    while (right - left > 1):

        middle = (left + right) // 2

        if first_type[middle] <= int(second_type[middle]):
            left = middle
        else:
            right = middle

    if (max(first_type[left], int(second_type[left])) < max(first_type[right], int(second_type[right]))):
        print(left)
    else:
        while right + 1 < l:
            
            if (first_type[right] == first_type[right + 1]):
                right += 1
            else:
                break
            
        print(right)

n, m, l = split_string(input())

first_type = [split_string(input()) for x in range(n)]
second_type = [input().split() for x in range(m)]

q = int(input())

for x in range(q):

    request = input().split()

    binary_search(first_type[int(request[0])], second_type[int(request[1])])

