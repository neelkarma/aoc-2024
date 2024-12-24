from collections import defaultdict
from itertools import combinations

pairs = []
with open("input.txt") as f:
    pairs = [tuple(line.rstrip().split("-")) for line in f]

graph = defaultdict(list)
for a, b in pairs:
    graph[a].append(b)
    graph[b].append(a)

trios = set()

for peer, others in graph.items():
    if peer[0] != "t":
        continue

    for a, b in combinations(others, 2):
        if b not in graph[a]:
            continue

        trios.add(tuple(sorted([peer, a, b])))

print(len(trios))
