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
    
    def next(self, root: Root):

        if not root:
            return None
        
        if root.right_branch:
            next_root = root.right_branch
            
            while next_root.left_branch:
                next_root = next_root.left_branch

            return next_root
        
        next_root = root

        while next_root.parent and next_root.parent.right_branch == next_root:
            next_root = next_root.parent

        return next_root.parent        

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

    @staticmethod
    def draw(root: Root, is_single_branch = True, string = None):

        if root == None:
            return

        if string == None:
            print(root.value)     
            new_string = ""
        
        elif is_single_branch:
            print(f"{string}└───{root.value}")
            new_string = string + "    "

        else:
            print(f"{string}├───{root.value}")
            new_string = string + "│   "

        Tree.draw(root.left_branch, not root.right_branch, new_string)
        Tree.draw(root.right_branch, True, new_string)

    def handle_request(self, request: List[str]):

        if request[0] == "print":
            Tree.draw(self.root)

        elif request[0] == "add":
            for number in request[1:]:
                self.add(int(number))
            print("Ok")

        elif request[0] == "delete":
            self.delete(self.find(int(request[1])))
            print("Ok")

        elif request[0] == "find":
            root = self.find(int(request[1]))
            if root:
                print("Число нашлось")
            else:
                print("Число не нашлось")

        elif request[0] == "next":
            next_root = self.next(self.find(int(request[1])))
            if next_root:
                print(next_root.value)
            else:
                print("Следующего числа нет")

array = [int(x) for x in input().split()]

tree = Tree(array)

while True:
    request = input().split()
    if request[0] == "exit":
        break
    else:
        tree.handle_request(request)