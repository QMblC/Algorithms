
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


def handle(queue):
    for i in range(int(input())):
        request = input().split()
        if "+" == request[0]:
            queue.push_last(request[1])
        elif "*" == request[0]:
            queue.push_middle(request[1])
        elif "!" == request[0]:
            queue.push_first(request[1])
        elif "-" ==  request[0]:
            print(queue.pop())

queue = DragonQueue()

handle(queue)