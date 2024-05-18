class Trie:
    class Node:
        def __init__(self) -> None:
            self.is_end = None
            self.children = {}

        def contains(self, char: str):
            return char in self.children

        def add_child(self, char: str):
            self.children[char] = Trie.Node()

        def get_child(self, char: str):
            return self.children[char]

    def __init__(self) -> None:
        self.root = Trie.Node()
        self.output = []

    def add(self, added: str, line: int, pos: int):
        node = self.root
        for char in added:
            if not node.contains(char):
                node.add_child(char)
                if node.is_end is None:
                    node.is_end = (line, pos)
            node = node.get_child(char)
        if node.is_end is None:
            node.is_end = (line, pos)

    def is_banned(self, word: str):
        node = self.root
        for char in word:
            if node.contains(char):
                node = node.get_child(char)
            else:
                return None
        return node.is_end

trie = Trie()

banned = []

n = int(input())

for i in range(n):
    word = input().strip().lower()
    banned.append(word)

m = int(input())

for i in range(m):
    line = input()
    words = line.split()
    position = 0
    for word in words:
        for index in range(len(word)):
            trie.add(word[index:].lower(), i + 1, position + 1 + index)
        position += len(word) + 1

min_ban = (float('inf'), float('inf'))
is_found = False

for word in banned:
    a = trie.is_banned(word)
    if a:
        if a < min_ban:
            min_ban = a
        is_found = True

if not is_found:
    print("Одобрено")
else:
    print(min_ban[0], min_ban[1])
