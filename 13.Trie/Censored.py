from functools import lru_cache

class Trie:
    class Node:
        def __init__(self) -> None:
            self.is_end = False
            self.children = [0] * 98

        def contains(self, char: str):
            return self.children[ord(char) - 30] != 0
        
        def add_child(self, char: str):
            self.children[ord(char) - 30] = Trie.Node()
        
        def get_child(self, char: str):
            return self.children[ord(char) - 30]

            
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

    @lru_cache
    def is_banned(self, word: str):
        node = self.root
        for char in word:
            if node.contains(char):
                node = node.get_child(char)
            else:
                return node.is_end
        
        return node.is_end
    
position = 0
    
trie = Trie()

n = int(input())

for i in range(n):
    word = input()
    trie.add(word.lower())

m = int(input())

is_found = False


for i in range(m):
    
    line = input()
    position = 0
    
    for index, word in enumerate(line.split()):

        length = len(word)

        for j in range(len(word)):
            part = word[j:]
        
            if trie.is_banned(part.lower()):
                is_found = True
                position += j

                print(i + 1, position + 1)    

                break

        if is_found:
            break

        position += length + 1

    if is_found:
        break

if not is_found:
    print("Одобрено")