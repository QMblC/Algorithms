from typing import List

class Dish:
    def __init__(self, index, price, calories) -> None:
        self.index = index
        self.price = price
        self.calories = calories

class Order:
    def __init__(self, indexes = [], calories = 0, cost = 0) -> None:
        self.indexes = indexes
        self.calories = calories
        self.cost = cost

    def add_dish(self, dish: Dish):
        self.indexes = self.indexes + [dish.index]
        self.calories += dish.calories
        self.cost += dish.price

    def copy(self):
        return Dish(self.indexes, self.calories, self.cost)

n, w = [int(x) for x in input().split()]

max_cal = 0
max_ind = []

dishes = []
for index in range(n):
    price, calories = [int(x) for x in input().split()]
    dishes.append(Dish(index + 1, price, calories))

def count(student_money, cost, dishes: List[Dish], calories, indexes: List[int], di = 0):
    if cost >= student_money or di + 1 == len(dishes):
        global max_cal
        global max_ind
        if calories > max_cal:
            max_cal = calories
            max_ind = indexes
        elif calories == max_cal:
            if len(indexes) > len(max_ind):
                max_ind = indexes
        return
    
    for di in range(di, len(dishes)):
        dish = dishes[di]
        if cost + dish.price <= student_money and not(dish.index in indexes):
            new_indexes = indexes + [dish.index]
            count(student_money, cost + dish.price, dishes, calories + dish.calories, new_indexes, di)


count(w,0,dishes,0,[])
print(len(max_ind), max_cal)
print(*max_ind, sep= " ")