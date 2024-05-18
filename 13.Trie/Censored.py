class Trie:
    class Node:
        def __init__(self) -> None:
            self.is_end = False
            self.children = dict()

        def contains(self, char: str):
            return char in self.children
        
        def add_child(self, char: str):
            self.children[char] = Trie.Node()
        
        def get_child(self, char: str):
            return self.children[char]

            
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
    
    for word in line.split():

        length = len(word)
        
        for j in range(length):

            if trie.is_banned(word[j:].lower()):

                print(i + 1, position + j + 1)
                is_found = True
                break

        if is_found:
            break

        position += length + 1

    if is_found:
        break

if not is_found:
    print("Одобрено")

