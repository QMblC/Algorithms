
queue = []

for i in range(int(input())):
    request = input().split()
    if "+" == request[0]:
        queue.append(int(request[1]))
    elif "*" == request[0]:
        middle = len(queue) // 2 + len(queue) % 2
        queue.insert(middle, int(request[1]))
    elif "!" == request[0]:
        queue.insert(0, int(request[1]))
    elif "-" ==  request[0]:
        print(queue.pop(0))