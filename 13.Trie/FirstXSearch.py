from typing import List

class Trie:
    class Node:
        def __init__(self) -> None:
            self.is_end = False
            self.children = [0] * 256

        def contains(self, char: str):
            return self.children[ord(char)] != 0
        
        def add_child(self, char: str):
            self.children[ord(char)] = Trie.Node()
        
        def get_child(self, char: str):
            return self.children[ord(char)]

            
    def __init__(self) -> None:
        self.root = Trie.Node()
        self.output = []

    def add(self, added: str):
        node = self.root

        for char in added:

            if not node.contains(char):
                node.add_child(char)

            node = node.get_child(char)

        node.is_end = True

    def get(self, prefix: str, count: int):
        node = self.root
        self.output = []

        for char in prefix:
            if node.contains(char):
                node = node.get_child(char)
            else:
                return

        self.get_recursion(node, node, prefix, count)

    def get_recursion(self, start: Node,  node: Node, prefix: str, count: int):

        if len(self.output) == count:    
            return
        
        if node.is_end and node != start:
            self.output.append(prefix)
        
        for index, child in enumerate(node.children):
            if child != 0:
                self.get_recursion(start, child, prefix + chr(index), count)


    def handle_request(self):
        while True:
            inputed = input().split()
            if inputed[0] == "exit":
                print("bye")
                break
            elif inputed[0] == "add":
                self.add(inputed[1])
                print("ok")
            elif inputed[0] == "get":
                self.get(inputed[1], int(inputed[2]))
                if self.output:
                    print(*self.output, sep = " ")
                else:
                    print("empty")
        
trie = Trie()
trie.handle_request()