from typing import List

class Node:
    def __init__(self, id: int, linked_nodes: List[int]) -> None:
        self.id = id
        self.linked = linked_nodes

n, v = [int(x) for x in input().split()]
nodes = []
stack = [v]
for id in range(n):

    nodes.append(Node(id, [int(x) for x in input().split()]))

def get_component(nodes: List[Node], stack: List[Node], component: List[int]):
    
    current_node_id = stack.pop(0)
    
    if nodes[current_node_id].linked == [-1]:
        return [current_node_id]
    if not(current_node_id in component):
        component.append(current_node_id)

    for node_id in nodes[current_node_id].linked:
        if not(node_id in component):
            stack.append(node_id)
    
    if len(stack) == 0:
        return sorted(component)
    get_component(nodes, stack, component)

    return sorted(component)

print(*get_component(nodes, stack, []), sep=" ")
