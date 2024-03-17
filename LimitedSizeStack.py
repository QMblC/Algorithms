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
            self.size += 1         
        else:
            self.first_item = My_Stack.Item(value, None, self.first_item)
            self.first_item.next_item.previous_item = self.first_item

            if self.last_item == None:
                self.last_item = self.first_item.next_item
                self.last_item.previous_item = self.first_item
            
            self.size += 1

            if self.limit < self.size:
                self.last_item = self.last_item.previous_item
                self.last_item.next_item = None
                self.size -= 1

        print("ok")   

    def pop(self):
        if (self.limit == 0):
            print(0)
            return
        print(self.first_item.value)
        self.first_item = self.first_item.next_item
        self.size -= 1

    def count(self):
        print(self.size)

stack = My_Stack(int(input()))

while True:
    request = input()
    if "push" in request:
        stack.push(request.split()[1])
    if "pop" in request:
        stack.pop()
    if "count" in request:
        stack.count()
    if "exit" in request:
        print("bye")
        break