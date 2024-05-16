from typing import List

class Cake:
    def __init__(self, id: int, price: int, volume: int, is_cutable: str) -> None:
        self.id = id
        self.price = price
        self.volume = volume
        self.ratio = price / volume
        self.is_cutable = is_cutable

    def __lt__(self, other):
        return self.ratio < other.ratio
    
class ThiefBag:
    def __init__(self, volume: int) -> None:
        self.volume_left = volume
        self.cost = 0

    def add(self, cake: Cake):
        if self.volume_left >= cake.volume:
            self.cost += cake.price
            self.volume_left -= cake.volume
        else:
            ratio = self.volume_left / cake.volume
            self.cost += cake.price * ratio
            self.volume_left = 0

def get_maximum_value(cakes: List[Cake], capacity: int):

    thief_bag = ThiefBag(capacity)
    for cake in cakes:
        if thief_bag.volume_left == 0:
            break
        if cake.is_cutable or (not cake.is_cutable and thief_bag.volume_left - cake.volume >= 0):
            thief_bag.add(cake)
        elif not cake.is_cutable and thief_bag.volume_left - cake.volume < 0:
            continue

    return thief_bag.cost

def get_data(n):

    cakes = []

    for i in range(n):

        price, volume, char = input().split()
        cake = Cake(i, int(price), int(volume), char == "Д")

        cakes.append(cake)

    return cakes

n, w = [int(x) for x in input().split()]
cakes = get_data(n)
cakes.sort(reverse=True)

print(format(get_maximum_value(cakes, w), ".2f"))