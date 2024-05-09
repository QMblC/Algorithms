from typing import List

class Cake:
    def __init__(self, id,  price: int, volume: int) -> None:
        self.id = id
        self.price = price
        self.volume = volume
        self.ratio = price / volume

class ThiefBag:
    def __init__(self, volume, ids = [], cost = 0) -> None:
        self.cost = cost
        self.volume_left = volume
        self.ids = ids

    def add_cake(self, cake: Cake):
        self.cost += cake.price
        self.volume_left -= cake.volume

        self.ids = self.ids + [cake.id]

        return self

    def add_cake_part(self, cake: Cake):
        cake_part_ratio = self.volume_left / cake.volume
        self.cost += cake.price * cake_part_ratio
        self.volume_left -= cake.volume * cake_part_ratio

        self.ids = self.ids + [cake.id]

        return self
    
    def copy(self):
        return ThiefBag(self.volume_left, self.ids, self.cost)


max_cost = 0

def count(cakes: List[Cake], thief_bag: ThiefBag, cake_index = 0):

    update_data(thief_bag)

    if thief_bag.volume_left <= 0 or cake_index == len(cakes):
        return
    
    for cake_index in range(len(cakes)):

        cake = cakes[cake_index]

        if cake.id in thief_bag.ids:
            continue

        new_tb = thief_bag.copy()

        if thief_bag.volume_left - cake.volume < 0: 
            count(cakes, new_tb.add_cake_part(cake), cake_index)

        else:
            count(cakes, new_tb.add_cake(cake), cake_index)

def update_data(thief_bag: ThiefBag):

    global max_cost
    if thief_bag.cost > max_cost:
        max_cost = thief_bag.cost
    

def get_data(n):

    cakes = []
    
    for i in range(n):

        price, volume = [int(x) for x in input().split()]
        cake = Cake(i, price, volume)

        cakes.append(cake)

    return cakes
n, w  = [int(x) for x in input().split()]

cakes = get_data(n)
count(cakes, ThiefBag(w))
print(format(max_cost,".2f"))