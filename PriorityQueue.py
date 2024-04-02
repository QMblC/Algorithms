import re
from typing import Dict

class Priority_Queue:

    class Inner_Queue:
        def __init__(self) -> None:
            self.first_item = 0
            self.last_item = 0
            self.body = []

        def push(self, value):
            
            self.body.append(value)
        
            self.last_item += 1  

        def pop(self):

            value = self.body[self.first_item]
            self.body[self.first_item] = None

            if self.first_item + 1 != len(self.body):
                self.first_item += 1

            return value
        
        def pop_all(self):
            return " ".join(self.body[self.first_item: self.last_item])
        
        def is_empty(self):
            return self.body[self.first_item] == None
        
    def __init__(self) -> None:
        self.first_item = 0
        self.last_item = 99999999999
        self.body = dict()
        self.size = 0

    def push(self, value, priority):

        if not(priority in self.body):
            self.body[priority] = Priority_Queue.Inner_Queue()
        self.body[priority].push(value)

        self.first_item = max(self.first_item, priority)
        self.last_item = min(self.last_item, priority)

        self.size += 1

        print("ok")

    def pop(self, priority):

        if not(priority in self.body):
            return -1

        value = self.body[priority].pop()
        if self.body[priority].is_empty():
            del self.body[priority]

        if len(self.body) != 0:
            self.first_item = max([x for x in self.body])
        else:
            self.first_item = 0
            self.last_item = 99999999999

        self.size -= 1
        return value
    
    def pop_top(self):

        if not(self.first_item in self.body):
            return -1

        value = self.body[self.first_item].pop()
        if self.body[self.first_item].is_empty():
            del self.body[self.first_item]

        if len(self.body) != 0:
            self.first_item = max([x for x in self.body])
        else:
            self.first_item = 0
            self.last_item = 99999999999

        self.size -= 1
        return value
    
    def pop_all(self, priority):

        if not(priority in self.body):
            return -1

        value = self.body[priority].pop_all()
        del self.body[priority]
        
        if len(self.body) != 0:
            self.first_item = max([x for x in self.body])
        else:
            self.first_item = 0
            self.last_item = 99999999999

        self.size -= len(value.split())
        return value
    
    def get_size(self):
        return self.size

    def clear(self):
        
        self.first_item = 0
        self.last_item = 99999999999
        self.body = dict()
        self.size = 0

        print("ok")

    def exit(self):
        print("bye")

queue = Priority_Queue()

while True:
    request = input()
    if re.match("size", request):
        print(queue.get_size())
    elif re.match("push", request):
        queue.push(request.split()[1], int(request.split()[2]))
    elif re.match("pop top", request):
        print(queue.pop_top())
    elif re.match("popall", request):
        print(queue.pop_all(int(request.split()[1])))
    elif re.match("pop", request):
        print(queue.pop(int(request.split()[1])))
    elif re.match("front", request):
        print(queue.front())
    elif re.match("view", request):
        print(queue.view())
    elif re.match("clear", request):
        queue.clear()
    elif re.match("exit", request):
        queue.exit()
        break