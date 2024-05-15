from typing import Dict, List
        
n =  int(input())
g = eval(input())
a, b = [int(x) for x in input().split()]

ancestors = []

def get_ancestors(g: Dict[int, int], arr: List[int],  element: int):

    global ancestors

    current_node = arr[-1]

    for child in g[current_node]:

        if child == element:
            ancestors = arr
            return

        else:
            if child in g:
                get_ancestors(g, arr + [child], element)
            else:
                continue
        
first_el = list(g.keys())[0]
get_ancestors(g,[first_el], a)
a_ancestors = ancestors

get_ancestors(g,[first_el], b)
b_ancestors = ancestors 

common = first_el
if a_ancestors and b_ancestors:
    for i in range(min(len(a_ancestors), len(b_ancestors))):
        if a_ancestors[i] == b_ancestors[i]:
            common = a_ancestors[i]
print(common)