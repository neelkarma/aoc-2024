from collections import defaultdict
from itertools import combinations

pairs = []
with open("input.txt") as f:
    pairs = [tuple(line.rstrip().split("-")) for line in f]

graph = defaultdict(list)
for a, b in pairs:
    graph[a].append(b)
    graph[b].append(a)

largest_network = set()

for peer, others in graph.items():
    network = set([peer] + others)

    for a, b in combinations(others, 2):
        if b not in graph[a]:
            network.discard(a)

    if len(network) > len(largest_network):
        largest_network = network

print(",".join(sorted(largest_network)))
