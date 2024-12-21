import itertools
from collections import deque

dim = 71
corrupted = set()
with open("input.txt") as f:
    for line in itertools.islice(f, 1024):
        x, y = map(int, line.rstrip().split(","))
        corrupted.add((x, y))

graph = {}
for y in range(dim):
    for x in range(dim):
        graph[(x, y)] = set()
        for px, py in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if not (0 <= px < dim and 0 <= py < dim):
                continue
            if (px, py) in corrupted:
                continue
            graph[(x, y)].add((px, py))

dists = {}
dists[(0, 0)] = 0
queue = deque([(0, 0)])
while queue:
    node = queue.popleft()
    for other in graph[node]:
        if other not in dists:
            dists[other] = dists[node] + 1
            queue.append(other)

print(dists[(dim - 1, dim - 1)])
