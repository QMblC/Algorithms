from typing import List

class Cake:
    def __init__(self, price: int, volume: int) -> None:
        self.price = price
        self.volume = volume
        self.ratio = price / volume
        

class ThiefBag:
    def __init__(self, volume) -> None:
        self.cost = 0
        self.start_volume = volume
        self.volume_left = volume
        self.reserve_cake = None
        self.reserve_ratio = 1

    def add(self, cake: Cake):
        self.cost += cake.price
        self.volume_left -= cake.volume

    def add_part(self, cake: Cake):
        cake_part_ratio = self.volume_left / cake.volume
        self.cost += cake.price * cake_part_ratio
        self.volume_left -= cake.volume * cake_part_ratio

    def add_reserve(self, cake: Cake):
        if self.reserve_cake != None:
            self.remove_reserve()

        if not(self.is_fit(cake)):         
            self.reserve_ratio = self.volume_left / cake.volume
        else:
            self.reserve_ratio = 1

        self.reserve_cake = cake
        
        self.cost += self.reserve_cake.price * self.reserve_ratio
        self.volume_left -= self.reserve_cake.volume * self.reserve_ratio

    def remove_reserve(self):
        self.cost -= self.reserve_cake.price * self.reserve_ratio
        self.volume_left += self.reserve_cake.volume * self.reserve_ratio

        self.reserve_cake = None

    def is_fit(self, cake: Cake):
        return self.volume_left - cake.volume >= 0
    

def get_sorted_data(n):

    

    max_cost = 0

    for i in range(n):

        price, volume = [int(x) for x in input().split()]
        inputed_cake = Cake(price, volume)
        thief_bag = ThiefBag(w)

        if len(cakes) == 0:
            
            cakes.append(inputed_cake)

            if thief_bag.is_fit(inputed_cake):
                thief_bag.add(inputed_cake)
            else:
                thief_bag.add_part(inputed_cake)

            max_cost = max(thief_bag.cost, max_cost)
            continue

        thief_bag.add_reserve(inputed_cake)

        for j in range(len(cakes)):
            current_cake = cakes[j]

            if inputed_cake in cakes:
                if thief_bag.is_fit(current_cake):
                    thief_bag.add(current_cake)
                    continue
                else:
                    thief_bag.add_part(current_cake)
                    break

            if j + 1 == len(cakes) and not(inputed_cake in cakes):
                if inputed_cake.ratio >= current_cake.ratio:
                    cakes.insert(j, inputed_cake)
                    thief_bag.remove_reserve()
                    if thief_bag.is_fit(inputed_cake):
                        thief_bag.add(inputed_cake)
                    else:
                        thief_bag.add_part(inputed_cake)
                else:
                    cakes.append(inputed_cake)
                    if thief_bag.is_fit(current_cake):
                        thief_bag.add(current_cake)
                    else:
                        thief_bag.add_part(current_cake)
                break

            elif inputed_cake.ratio >= current_cake.ratio:
                cakes.insert(j, inputed_cake)
                thief_bag.remove_reserve()
                if thief_bag.is_fit(inputed_cake):
                    thief_bag.add(inputed_cake)
                else:
                    thief_bag.add_part(inputed_cake)

            elif inputed_cake.ratio < cakes[j].ratio and thief_bag.is_fit(current_cake):
                thief_bag.add(current_cake)

            elif inputed_cake.ratio < cakes[j].ratio and not(thief_bag.is_fit(current_cake)):
                thief_bag.remove_reserve()
                if thief_bag.is_fit(current_cake):
                    thief_bag.add(current_cake)
                    thief_bag.add_reserve(inputed_cake)
                else:
                    thief_bag.add_part(current_cake)
                    break

        max_cost = max(thief_bag.cost, max_cost)
    return max_cost


n, w  = [int(x) for x in input().split()]
cakes = []
max_cost = get_sorted_data(n)


print(format(max_cost, ".2f"))