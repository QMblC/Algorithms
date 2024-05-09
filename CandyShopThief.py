from typing import List
import math

class Cake:
    def __init__(self, price: int, volume: int) -> None:
        self.price = price
        self.volume = volume
        self.ratio = price / volume

    def __lt__(self, other):
        return self.ratio < other.ratio

class ThiefBag:
    def __init__(self, volume) -> None:
        self.cost = 0
        self.start_volume = volume
        self.volume_left = volume

    def add_cake(self, cake: Cake):
        self.cost += cake.price
        self.volume_left -= cake.volume

    def add_cake_part(self, cake: Cake):
        cake_part_ratio = self.volume_left / cake.volume
        self.cost += cake.price * cake_part_ratio
        self.volume_left -= cake.volume * cake_part_ratio
    


def get_sorted_data(n):
    cakes = []
    for i in range(n):

        price, volume = [int(x) for x in input().split()]
        cake = Cake(price, volume)
        cakes.append(cake)

    a = sorted(cakes, reverse=True)
    return a

def fill_thief_bag(cakes: List[Cake]):
    thief_bag = ThiefBag(w)
    for cake in cakes:
        if thief_bag.volume_left - cake.volume == 0:
            thief_bag.add_cake(cake)
            break
        elif thief_bag.volume_left - cake.volume < 0:
            thief_bag.add_cake_part(cake)
            break
        else:
            thief_bag.add_cake(cake)
    return thief_bag
n, w  = [int(x) for x in input().split()]

cakes = get_sorted_data(n)

cost = str(round(fill_thief_bag(cakes).cost,2))

if cost[-2] == '.':
    print(cost + '0')
elif not('.' in cost):
    print(cost + ".00")
else:
    print(cost)