from typing import List

class Dish:
    def __init__(self, id, price: int, calories: int) -> None:
        self.id = id
        self.price = price
        self.calories = calories    

class Order:
    def __init__(self, student_money = 0, indexes = [], calories = 0, cost = 0) -> None:
        self.indexes = indexes
        self.calories = calories
        self.cost = cost
        self.student_money = student_money

    def add_dish(self, dish: Dish):
        self.indexes = self.indexes + [dish.id]
        self.calories += dish.calories
        self.cost += dish.price

        return self

    def copy(self):
        new_order = Order(self.student_money, self.indexes, self.calories, self.cost)
        return new_order

n, w = [int(x) for x in input().split()]

max_cal = 0
max_ind = []

dishes = []
for index in range(n):
    price, calories = [int(x) for x in input().split()]
    dishes.append(Dish(index + 1, price, calories))

def count(dishes: List[Dish], order: Order, dish_index = 0):

    if order.cost >= order.student_money or dish_index + 1 == len(dishes):
        global max_cal
        global max_ind
        if order.calories > max_cal:
            max_cal = order.calories
            max_ind = order.indexes
        elif order.calories == max_cal and len(order.indexes) > len(max_ind):
            max_ind = order.indexes
        return
    
    for dish_index in range(dish_index, len(dishes)):
        dish = dishes[dish_index]
        if order.cost + dish.price <= order.student_money and not(dish.id in order.indexes):
            new_order = order.copy()
            count(dishes, new_order.add_dish(dish), dish_index)


count(dishes, Order(w))
print(len(max_ind), max_cal)
print(*max_ind, sep= " ")