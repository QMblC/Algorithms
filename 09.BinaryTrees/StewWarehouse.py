from typing import List

class Root:
    def __init__(self, value: int, parent = None, left_branch = None, right_branch = None) -> None:
        self.value = value
        self.parent = parent
        self.left_branch = left_branch
        self.right_branch = right_branch
    
    def delete_branch(self):

        if self.parent.left_branch == self:
            self.parent.left_branch = None
        else:
            self.parent.right_branch = None

class Tree:
    def __init__(self, array: List[int]) -> None:
        self.root = self.create_tree(array, 0, len(array))

    def create_tree(self, array: List[int], left: int, right: int):

        if right - left < 1:
            return None
        
        if right - left == 1:
            return Root(array[left])
        
        middle = (left + right - 1) // 2

        root = Root(array[middle])
        root.left_branch = self.create_tree(array, left, middle)
        if root.left_branch:
            root.left_branch.parent = root
        root.right_branch = self.create_tree(array, middle + 1, right)
        if root.right_branch:
            root.right_branch.parent = root

        return root

    def add(self, number: int):
        root = self.root
        if not root:
            self.root = Root(number)
            return
        while root:
            if number < root.value:
                if not root.left_branch:
                    root.left_branch = Root(number, root)
                    break
                root = root.left_branch
            else:
                if not root.right_branch:
                    root.right_branch = Root(number, root)
                    break
                root = root.right_branch

    def find(self, number):
        root = self.root
        while root:
            if root.value == number:          
                return root
            elif number < root.value:
                root = root.left_branch
            else:
                root = root.right_branch
        return None
    
    def find_deleted_root(self, number: int):

        root = self.find(number)
        if not root:
            return
        
        self.delete(root)

    def delete(self, root: Root):
        if not root:
            return
        
        if not root.left_branch or not root.right_branch:
            branch = None
            if root.left_branch:
                branch = root.left_branch
            else:
                branch = root.right_branch

            if root == self.root:
                self.root = branch
                if not branch:
                    branch.parent = None
            
            if root.parent.left_branch == root:
                root.parent.left_branch = branch
                if branch:
                    branch.parent = root.parent
            
            else:
                root.parent.right_branch = branch
                if branch:
                    branch.parent = root.parent
        else:
            next_root = root.right_branch
            while next_root.left_branch:
                next_root = next_root.left_branch
            root.value = next_root.value
            self.delete(next_root)
    def get_min(self):
        root = self.root
        if not root:
            return None
        while root.left_branch:
            root = root.left_branch

        return root

    def get_max(self):
        root = self.root

        if not root:
            return None

        while root.right_branch:
            root = root.right_branch

        return root
    
    def get_list(self, root: Root):
        if not root:
            return
        
        self.get_list(root.left_branch)
        if root != self.get_max():
            print(root.value, end = " ")
        else:
            print(root.value)
        self.get_list(root.right_branch)

    def handle_request(self, request: List[str]):

        if request[0] == "print":
            Tree.draw(self.root)

        elif request[0] == "add":
            for number in request[1:]:
                self.add(int(number))
            print("Ok")

        elif request[0] == "delete":
            self.find_deleted_root(int(request[1]))
            print("Ok")

        elif request[0] == "find":
            root = self.find(int(request[1]))
            if root:
                print("Такая банка есть")
            else:
                print("Такой банки нет")

        elif request[0] == "min":
            root = self.get_min()
            if not root:
                print("Склад пуст")
            else:
                print(root.value)
        
        elif request[0] == "max":
            root = self.get_max()
            if not root:
                print("Склад пуст")
            else:
                print(root.value)

        elif request[0] == "list":
            if self.root:
                self.get_list(self.root)
            else:
                print()

array = [int(x) for x in input().split()]

tree = Tree(array)

while True:
    request = input().split()
    if request[0] == "exit":
        break
    else:
        tree.handle_request(request)