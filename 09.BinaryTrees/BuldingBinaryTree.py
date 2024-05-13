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


array = [int(x) for x in input().split()]

tree = Tree(array)
Tree.draw(tree.root)