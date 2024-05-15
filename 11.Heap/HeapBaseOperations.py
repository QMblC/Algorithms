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

heap = Heap()
heap.handle_request()