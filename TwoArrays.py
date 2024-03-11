first_array = [int(x) for x in input().split()]
second_array = [int(x) for x in input().split()]

class Counter:
    def __init__(self) -> None:
        self.positive_items = []
        self.negative_items = []

    def resize(self, new_size: int):
        if new_size >= 0:
            for i in range(len(self.positive_items), new_size):
                self.positive_items.append(0)
        else:
            new_size = abs(new_size)
            for i in range(len(self.negative_items), new_size):
                self.negative_items.append(0)

    def __getitem__(self, index):
        if index >= 0:
            if index >= len(self.positive_items):
                self.resize(index + 1)
            return self.positive_items[index]
        else:
            if abs(index) >= len(self.negative_items):
                self.resize(index)
            return self.negative_items[abs(index) - 1]

    def increase_counter(self, index):

        if index >= 0:
            if index >= len(self.positive_items):
                self.resize(index + 1)
            
            self.positive_items[index] += 1
        else:
            
            if abs(index) >= len(self.negative_items):
                self.resize(index)
            
            self.negative_items[abs(index) - 1] += 1

counter = Counter()

for item in second_array:
    counter.increase_counter(item)

for index, item in enumerate(first_array):
    if index == len(first_array) - 1:
        ending = ""
    else:
        ending = " "

    print(counter[item], end = ending)

"""
-1 2 4 5 1 7 2 8 8 9 2 18 4
2 9 17 828 -2 -1
"""