import re

class DragonQueue:
    def __init__(self) -> None:
        self.body = []

    def push_last(self, value):
        self.body.append(value)

    def push_middle(self, value):
        middle = len(self.body) // 2 + len(self.body) % 2
        self.body.insert(middle, value)

    def push_first(self, value):
        self.body.insert(0, value)

    def pop(self):
        return self.body.pop(0)

queue = DragonQueue()

for i in range(int(input())):
    request = input()
    if re.match("\+", request):
        queue.push_last(request.split()[1])
    elif re.match("\*", request):
        queue.push_middle(request.split()[1])
    elif re.match("\!", request):
        queue.push_first(request.split()[1])
    elif re.match("\-", request):
        print(queue.pop())