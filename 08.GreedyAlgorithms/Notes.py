class Node:
    def __init__(self, char: str, frequency: int):
        self.char = char
        self.frequency = frequency
        self.node_zero = None
        self.node_one = None

    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __gt__(self, other):
        return self.frequency > other.frequency

def dfs(node, length = 0):
    if not node:
        return 0
    elif node.node_zero == None and node.node_one == None:
        return length * node.frequency
    else:
        length0 = dfs(node.node_zero, length + 1)
        length1 = dfs(node.node_one, length + 1)
        
        return length0 + length1
    
def create_queue(string: str):
    frequency = {}
    for char in string:
        if not(char in frequency):
            frequency[char] = 0
        frequency[char] += 1

    queue = []

    for char, freq in frequency.items():
        queue.append(Node(char, freq))

    return sorted(queue)
    
def huffman(string: str):
    
    queue = create_queue(string)

    while len(queue) > 1:

        zero = queue.pop(0)
        one = queue.pop(0)
        node = Node(None, zero.frequency + one.frequency)
        node.node_zero = zero
        node.node_one = one
        queue.append(node)
        queue.sort()
        
    if queue[0].node_zero == None and queue[0].node_one == None:
        return 1
    return dfs(queue[0])

input_string = input()
print(huffman(input_string))


#abracadabra