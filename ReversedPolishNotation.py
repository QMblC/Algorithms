

class My_Stack:
    class Item:
        def __init__(self, value, next) -> None:
            self.value = value
            self.next_item = next

    def __init__(self) -> None:
        self.size = 0
        self.first_item = None


    def push(self, value):
        if self.size == 0:
            self.first_item = My_Stack.Item(value, None)          
        else:
            self.first_item = My_Stack.Item(value, self.first_item)

        self.size += 1

    def pop(self):
        value = self.first_item.value
        self.first_item = self.first_item.next_item
        self.size -= 1
        return value
    
opearations = ['+', '-', '/', '*', '%']
stack = My_Stack()

for i in input().split():
    if not i in opearations:
        stack.push(int(i))
    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.push(a + b)
        elif i == '-':
            stack.push(a - b)
        elif i == '/':
            stack.push(a // b)
        elif i == '*':
            stack.push(a * b)
        elif i == '%':
            stack.push(a % b)

print(stack.pop())
