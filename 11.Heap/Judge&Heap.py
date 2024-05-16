class Cake:
    def __init__(self, price: int, volume: int) -> None:
        self.price = price
        self.volume = volume
        self.ratio = price / volume

    def __lt__(self, other):
        return self.ratio < other.ratio
    
    def __gt__(self, other):
        return self.ratio > other.ratio
    
class Heap:
    def __init__(self) -> None:
        self.body = []
    
    def get_max(self):
        return self.body[0]
    
    def get_size(self):
        return len(self.body)

    def add(self, number: int):

        self.body.append(number)
        index = self.get_size() - 1
        parent_index = (index - 1) // 2

        while self.body[index] > self.body[parent_index]:
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

            max_child = left

            if right < self.get_size() and self.body[right] > self.body[left]:
                max_child = right

            if self.body[max_child] > self.body[index]:
                self.body[index], self.body[max_child] = self.body[max_child], self.body[index]

            index = max_child
        
n, w = [int(x) for x in input().split()]
cakes = Heap()

for i in range(n):
    price, volume = map(int, input().split())
    cakes.add(Cake(price, volume))

volume_sum = 0
cost = 0

while volume_sum < w:

    cake = cakes.pop()
    if not cake:
        break
    
    if volume_sum + cake.volume <= w:
        volume_sum += cake.volume
        cost += cake.price
    else:
        
        cost += ((w - volume_sum) / cake.volume) * cake.price
        volume_sum = w

print(format(cost, ".2f"))
