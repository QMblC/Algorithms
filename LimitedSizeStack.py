import re

class My_Stack:

    class Item:
        def __init__(self, value, previous, next) -> None:
            self.value = value
            self.previous_item = previous
            self.next_item = next
            
    def __init__(self, limit) -> None:
        self.limit = limit
        self.size = 0
        self.first_item = None
        self.last_item = None

    def push(self, value):
        if (self.limit == 0):
            print("ok")
            return

        if self.size == 0:
            self.first_item = My_Stack.Item(value, None, None)
            self.last_item = self.first_item       
        else:
            self.first_item = My_Stack.Item(value, None, self.first_item)
            self.first_item.next_item.previous_item = self.first_item
            
        self.size += 1

        if self.limit < self.size:
            self.last_item = self.last_item.previous_item
            self.last_item.next_item = None
            self.size -= 1 
        
        print("ok")

    def pop(self):
        print(self.first_item.value)
        self.first_item = self.first_item.next_item
        self.size -= 1

    def count(self):
        print(self.size)

stack = My_Stack(int(input()))

while True:
    request = input()

    if re.match("push", request):
        stack.push(request.split()[1])  
    if re.match("pop", request):
        stack.pop()
    if re.match("count", request):
        stack.count()
    if re.match("exit", request):
        print("bye")
        break