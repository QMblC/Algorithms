from typing import List

class Root:
    def __init__(self, value: int, depth: int, left_branch = None, right_branch = None) -> None:
        self.value = value
        self.depth = depth
        self.left_branch = left_branch
        self.right_branch = right_branch

class Tree:
    def __init__(self, array: List[int]) -> None:
        self.root = self.create_tree(array, 0, len(array))

    def create_tree(self, array: List[int], left: int, right: int, depth = 0):

        if right - left < 1:
            return None
        
        if right - left == 1:
            return Root(array[left], depth)
        
        middle = (left + right - 1) // 2

        root = Root(array[middle], depth)
        root.left_branch = self.create_tree(array, left, middle, depth + 1)
        root.right_branch = self.create_tree(array, middle + 1, right, depth + 1)

        return root

    def add(self, number: int):
        root = self.root
        while root:
            if number < root.value:
                if not root.left_branch:
                    root.left_branch = Root(number, root.depth + 1)
                    break
                root = root.left_branch
            else:
                if not root.right_branch:
                    root.right_branch = Root(number, root.depth + 1)
                    break
                root = root.right_branch

    def find(self, number):
        root = self.root
        while root:
            if root.value == number:          
                return "Число нашлось"
            elif number < root.value:
                root = root.left_branch
            else:
                root = root.right_branch
        return "Число не нашлось"
    
    def next(self, number):
        root = self.root
        next_value = None
            
        while root:
            if number < root.value:
                next_value = root.value
                root = root.left_branch
            else:
                root = root.right_branch

        if not next_value:
            next_value = "Следующего числа нет"
        return next_value
            
    def delete(self, number: int):
        root = self.root
        root_deleted_branch = None
        if root.value != number:
            while root:
                if number < root.value:
                    root_deleted_branch = root
                    root = root.left_branch
                elif number > root.value:
                    root_deleted_branch = root
                    root = root.right_branch
                else:
                    break
            
            if root.left_branch and root.right_branch:
                if root.value < root_deleted_branch.value:
                    new_root = self.get_optimal(number)
                    
                    new_root.left_branch = root.left_branch
                    new_root.right_branch = root.right_branch

                    root_deleted_branch.left_branch = new_root
                else:
                    new_root = self.get_optimal(number)
                    
                    new_root.left_branch = root.left_branch
                    new_root.right_branch = root.right_branch

                    root_deleted_branch.right_branch = new_root

            elif root.left_branch and not root.right_branch:
                if root.value < root_deleted_branch.value:
                    root_deleted_branch.left_branch = root.left_branch
                else:
                    root_deleted_branch.right_branch = root.left_branch

            elif not root.left_branch and root.right_branch:
                if root.value < root_deleted_branch.value:
                    root_deleted_branch.left_branch = root.right_branch
                else:
                    root_deleted_branch.right_branch = root.right_branch

            else:
                if root.value < root_deleted_branch.value:
                    root_deleted_branch.left_branch = None
                else:
                    root_deleted_branch.right_branch = None

    def get_optimal(self, number):
        root = self.root
        optimal_root = None
            
        while root:
            if number < root.value:
                optimal_root = root
                root = root.left_branch
            else:
                root = root.right_branch

        return optimal_root

    @staticmethod
    def draw(root: Root, is_single_branch = True, string = ""):

        if root == None:
            return

        if root.depth == 0:
            print(root.value)     
            new_string = string + ""
        
        elif is_single_branch:
            print(f"{string}└───{root.value}")
            new_string = string + "    "

        else:
            print(f"{string}├───{root.value}")
            new_string = string + "│   "

        Tree.draw(root.left_branch, False, new_string)
        Tree.draw(root.right_branch, True, new_string)

    def handle_request(self, request: List[str]):
        if request[0] == "print":
            Tree.draw(self.root)
        elif request[0] == "add":
            for number in request[1:]:
                self.add(int(number))
            print("Ok")
        elif request[0] == "delete":
            self.delete(int(request[1]))
        elif request[0] == "find":
            print(self.find(int(request[1])))
        elif request[0] == "next":
            print(self.next(int(request[1])))


array = [int(x) for x in input().split()]

tree = Tree(array)

while True:
    request = input().split()
    if request[0] == "exit":
        break
    else:
        tree.handle_request(request)

Tree.draw(tree.root)