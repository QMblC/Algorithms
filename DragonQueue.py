import re

class DragonQueue:
    def __init__(self) -> None:
        self.body = []
        self.prince = None
        self.size = 0

    def push_last(self, value):
        self.body.append(value)
        self.size += 1

    def push_middle(self, value):
        middle = len(self.body) // 2
        if len(self.body) % 2 != 0:
            middle += 1
        self.body.insert(middle, value)
        self.size += 1

    def push_first(self, value):
        self.body.insert(0, value)

    def pop(self):
        if self.prince == None:
            value = self.body[0]
            del self.body[0]
            
        self.size -= 1
        return value

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