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
    
    def next(self, number):
        root = self.root
        next_root = None
        
        while root:
            if number < root.value:
                next_root = root
                root = root.left_branch
            else:
                root = root.right_branch

        if not next_root:
            return None
        return next_root
    
            
    def delete(self, number: int):
        root = self.find(number)

        if not root:
            return
        
        if not root.right_branch and not root.left_branch:
            root.delete_branch()
        
        elif root.right_branch and root.left_branch:
            subsitude = self.get_substitude(root)
            if subsitude.parent == root:
                root.value = subsitude.value
                subsitude.delete_branch()
                root.right_branch = subsitude.right_branch
            else:
                root.value = subsitude.value
                subsitude.delete_branch()
        
        else:

            if root.left_branch:
                if root.parent.left_branch == root:
                    root.parent.left_branch = root.left_branch
                    root.left_branch.parent = root.parent

                elif root.parent.right_branch == root:
                    root.parent.right_branch = root.left_branch
                    root.left_branch.parent = root.parent
            else:
                if root.parent.left_branch == root:
                    root.parent.left_branch = root.right_branch
                    root.right_branch.parent = root.parent

                elif root.parent.right_branch == root:
                    root.parent.right_branch = root.right_branch
                    root.right_branch.parent = root.parent

            if root.parent.left_branch == root:

                if root.left_branch:
                    root.parent.left_branch = root.left_branch
                    root.left_branch.parent = root.parent               
                else:
                    root.parent.left_branch = root.right_branch
                    root.right_branch.parent = root.parent     
                
            elif root.parent.right_branch == root:
                if root.right_branch:
                    root.parent.right_branch = root.left_branch
                    root.right_branch.parent = root.parent               
                else:
                    root.parent.right_branch = root.right_branch
                    root.left_branch.parent = root.parent

    def get_substitude(self, root: Root):
        start = root

        if root.right_branch:
            root = root.right_branch

        while root.left_branch:
            root = root.left_branch

        if start == root:
            return None
        return root

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
            self.delete(int(request[1]))
            print("Ok")
        elif request[0] == "find":
            root = self.find(int(request[1]))
            if root:
                print("Число нашлось")
            else:
                print("Число не нашлось")
        elif request[0] == "next":
            next_root = self.next(int(request[1]))
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