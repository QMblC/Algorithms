import re

class My_Queue:
    class Item:
        def __init__(self, value) -> None:
            self.value = value
            self.next_item = None

    def __init__(self) -> None:
        self.size = 0
        self.first_item = None
        self.last_item = None

    def push(self, value):
        
        last = My_Queue.Item(value)
        self.last_item = last

        if self.size == 0:
            self.first_item = last
                 
        else:
            self.last_item.next_item = last

            if self.first_item.next_item == None:
                self.first_item.next_item = self.last_item

        self.size += 1

        print("ok")

    def pop(self):
        value = self.first_item.value

        if self.size == 1:
            self.last_item = None
            self.first_item = None
        else:
            self.first_item = self.first_item.next_item
        self.size -= 1

        return value

    def front(self):
        return self.first_item.value
    
    def get_size(self):
        return self.size
    
    def view(self):
        current_item = self.first_item
        while True:
            if current_item.next_item == None:
                print(current_item.value, end = "\n")
                break
            else:
                print(current_item.value, end = ", ")
                current_item = current_item.next_item

    def clear(self):
        self.size = 0
        self.first_item = None
        self.last_item = None
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
        queue.view()
    elif re.match("clear", request):
        queue.clear()
    elif re.match("exit", request):
        queue.exit()
        break