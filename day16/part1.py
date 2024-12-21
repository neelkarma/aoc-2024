import heapq

from common import Direction, find_start_end, make_graph, read_input

grid = read_input("input.txt")
(xi, yi), (xf, yf) = find_start_end(grid)
graph = make_graph(grid)

dists = {}
start = xi, yi, Direction.EAST

queue = [(0, start)]
while queue:
    dist, node = heapq.heappop(queue)

    if node in dists:
        continue

    dists[node] = dist
    for other, edge in graph[node].items():
        if other not in dists:
            heapq.heappush(queue, (dist + edge, other))

ends = [(xf, yf, d) for d in Direction]
answer = min(dists[end] for end in ends)
print(answer)
