class Bacteria:
    def __init__(self, min_t, max_t) -> None:
        self.min_t = min_t
        self.max_t = max_t
    
n = int(input())
bacteria = []

for i in range(n):
    min_t, max_t = [int(x) for x in input().split()]
    bacteria.append(Bacteria(min_t, max_t))

for planet_temp in [int(x) for x in input().split()]:
    counter = 0
    for microbe in bacteria:
        if microbe.min_t <= planet_temp <= microbe.max_t:
            counter += 1
    print(counter)
