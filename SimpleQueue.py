import re

class My_Queue:
    def __init__(self) -> None:
        self.first_item = 0
        self.last_item = 0
        self.body = []
        

    def push(self, value):

        self.body.append(value)

        self.last_item += 1

        print("ok")

    def pop(self):

        value = self.body[self.first_item]
        self.body[self.first_item] = None
        self.first_item += 1

        return value

    def front(self):
        return self.body[self.first_item]
    
    def get_size(self):
        return len(self.body)
    
    def view(self):
        return ", ".join(self.body)

    def clear(self):
        self.first_item = 0
        self.last_item = 0
        self.body = []

        print("ok")

    def exit(self):
        print("bye")

queue = My_Queue()

while True:
    request = input()
    if re.match("size", request):
        print(queue.get_size())
    elif re.match("push", request):
        queue.push(request.split()[1])
    elif re.match("pop", request):
        print(queue.pop())
    elif re.match("front", request):
        print(queue.front())
    elif re.match("view", request):
        print(queue.view())
    elif re.match("clear", request):
        queue.clear()
    elif re.match("exit", request):
        queue.exit()
        break