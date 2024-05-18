class Trie:
    class Node:
        def __init__(self) -> None:
            self.counter = 0
            self.children = [0] * 128

        def contains(self, char: str):
            return self.children[ord(char) - ord("А") + 30] != 0
        
        def add_child(self, char: str):
            self.children[ord(char) - ord("А") + 30] = Trie.Node()
        
        def get_child(self, char: str):
            return self.children[ord(char) - ord("А") + 30]

            
    def __init__(self) -> None:
        self.root = Trie.Node()
        self.output = []
        self.out_counter = 0

    def add(self, added: str):
        node = self.root

        for char in added:

            if not node.contains(char):
                node.add_child(char)

            node = node.get_child(char)

        node.counter += 1

    def get(self, prefix):
        node = self.root

        self.output = ""
        self.out_counter = 0

        for char in prefix:
            if node.contains(char):
                node = node.get_child(char)
            else:
                return
                    

        self.get_auto_completion(prefix, node)
    
    def get_auto_completion(self, string: str, node: Node):
        if node.counter > 0:
            if self.out_counter < node.counter:      
                self.output = string
                self.out_counter = node.counter
            elif self.out_counter == node.counter:
                if len(self.output) > len(string):
                    self.output = string
                    self.out_counter = node.counter

        for index, child in enumerate(node.children):
            if child != 0 :
                char = chr(index + ord("А") - 30)
                self.get_auto_completion(string + char, node.get_child(char))

    def handle_request(self):
        while True:
            inputed = input().split()
            if inputed[0] == "exit":
                print("bye")
                break
            elif inputed[0] == "+":
                self.add(inputed[1])
                print("ok")
            elif inputed[0] == "?":
                if len(inputed) == 1:
                    string = ""
                else:
                    string = inputed[1]
                    
                self.get(string)
                if self.output == "":
                    print(None)
                else:
                    print(self.output)
        
trie = Trie()

for word in input().split():
    trie.add(word)
trie.handle_request()