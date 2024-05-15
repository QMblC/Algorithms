class Heap:
    def __init__(self) -> None:
        self.body = []
    
    def get_min(self):
        return self.body[0]
    
    def get_size(self):
        return len(self.body)

    def add(self, number: int):
        self.body.append(number)
        index = self.get_size() - 1
        parent_index = (index - 1) // 2
        while self.body[index] < self.body[parent_index]:
            self.body[index], self.body[parent_index] = self.body[parent_index], self.body[index]
            index = parent_index
            parent_index = (index - 1) // 2
            if index == 0:
                break

    def pop(self):

        if self.get_size() == 0:
            return
        elif self.get_size() == 1:
            return self.body.pop()
        else:
            self.body[0], self.body[-1] = self.body[-1], self.body[0]
            deleted = self.body.pop()
            self.fix_heap()

            return deleted

    def fix_heap(self):
        index = 0
        while index * 2 + 1 < self.get_size():
            left = index * 2 + 1
            right = index * 2 + 2

            min_child = left

            if right < self.get_size() and self.body[right] < self.body[left]:
                min_child = right

            if self.body[min_child] < self.body[index]:
                self.body[index], self.body[min_child] = self.body[min_child], self.body[index]

            index = min_child
        
        
    def get_structure(self):
        print("---STRUCTURE START---")
        start = 1
        if not self.body:
            print("---STRUCTURE END---")
            return
        print(self.body[0])
        i = 1
        while 2 ** i <= self.get_size(): 
            print(*self.body[start : min(start + 2 ** i, self.get_size())], sep= " ")
            start += 2 ** i
            i += 1

        print("---STRUCTURE END---")

    def handle_request(self):
        
        while True:
            inputed_string = input().split()
            request = inputed_string[0]

            if request == "add":
                self.add(int(inputed_string[1]))
                print("ok")
            elif request == "min":
                print(self.get_min())
            elif request == "size":
                print(self.get_size())
            elif request == "exit":
                print("bye")
                break
            elif request == "pop":
                
                print(self.pop())
            elif request == "structure":
                self.get_structure()

heap = Heap()
heap.handle_request()