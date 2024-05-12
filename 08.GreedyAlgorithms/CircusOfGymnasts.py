from typing import List

class Gymnast:
    def __init__(self, name: str, lifted_weight: int, weight: int) -> None:
        self.name = name
        self.lifted_weight = lifted_weight
        self.weight = weight
        self.weight_sum = weight + lifted_weight

    def __lt__(self, other):
        return self.weight_sum < other.weight_sum
    
class Tower:
    def __init__(self) -> None:
        self.weight = 0
        self.active_gymnasts = []
        self.counter = 0

    def add(self, gymnast: Gymnast):
        self.counter += 1
        self.weight += gymnast.weight
        self.active_gymnasts.append(gymnast)
        self.active_gymnasts.sort(key= lambda x: x.weight)
    
    def change(self, gymnast: Gymnast):
        self.weight -= self.active_gymnasts[-1].weight
        self.active_gymnasts.pop()
        self.active_gymnasts.append(gymnast)
        self.weight += gymnast.weight
        self.active_gymnasts.sort(key= lambda x: x.weight)


def get_gymnasts():
    n = int(input())

    gymnasts = []

    for i in range(n):
        name, lifted_weight, weight = [x for x in input().split(';')]
        gymnasts.append(Gymnast(name, int(lifted_weight), int(weight)))

    return gymnasts

def solve(gymnasts: List[Gymnast]):
    tower = Tower()
    gymnasts.sort()

    for i in range(len(gymnasts)):
        if gymnasts[i].lifted_weight >= tower.weight:
            tower.add(gymnasts[i])

        else:
            if tower.active_gymnasts[-1].weight > gymnasts[i].weight:
                tower.change(gymnasts[i])

    return tower.counter

gymnasts = get_gymnasts()

print(solve(gymnasts))