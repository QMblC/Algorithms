from typing import List

class Cake:
    def __init__(self, price: int, volume: int) -> None:
        self.price = price
        self.volume = volume
        self.ratio = price / volume

    def __lt__(self, other):
        return self.ratio < other.ratio

class ThiefBag:
    def __init__(self, volume: int) -> None:
        self.volume = volume
        self.cost = 0

    def add(self, cake: Cake):
        if self.volume >= cake.volume:
            self.cost += cake.price
            self.volume -= cake.volume
        else:
            ratio = self.volume / cake.volume
            self.cost += cake.price * ratio
            self.volume = 0

def get_maximum_value(cakes: List[Cake], capacity: int):
    cakes.sort(reverse=True)

    thief_bag = ThiefBag(capacity)
    for cake in cakes:
        if thief_bag.volume == 0:
            break
        thief_bag.add(cake)
    return thief_bag.cost

n, w = [int(x) for x in input().split()]
cakes = []

for i in range(n):
    price, volume = map(int, input().split())
    cakes.append(Cake(price, volume))

max_val = get_maximum_value(cakes, w)
print(format(max_val, ".2f"))