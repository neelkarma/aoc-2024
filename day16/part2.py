import heapq
from collections import deque

from common import Direction, find_start_end, make_graph, read_input

grid = read_input("input.txt")
(xi, yi), (xf, yf) = find_start_end(grid)
graph = make_graph(grid)

start = xi, yi, Direction.EAST

dists = {}
prev = {}
dists[start] = 0

queue = [(0, start)]
while queue:
    dist, node = heapq.heappop(queue)

    dists[node] = dist

    for other, edge in graph[node].items():
        other_dist = dists.get(other, float("inf"))
        alt = dists.get(node, float("inf")) + edge

        if alt == other_dist:
            prev[other].append(node)
        elif alt < other_dist:
            dists[other] = alt
            prev[other] = [node]
            heapq.heappush(queue, (alt, other))

end = min([(xf, yf, d) for d in Direction], key=lambda n: dists[n])

tiles = set()
queue = deque([end])
while queue:
    node = queue.popleft()
    tiles.add((node[0], node[1]))
    for prev_node in prev.get(node, []):
        queue.append(prev_node)

print(len(tiles))
