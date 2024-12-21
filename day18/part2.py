from collections import deque

dim = 71
corrupted = []
with open("input.txt") as f:
    for line in f:
        x, y = map(int, line.rstrip().split(","))
        corrupted.append((x, y))


graph: dict[tuple[int, int], set[tuple[int, int]]] = {}
for y in range(dim):
    for x in range(dim):
        graph[(x, y)] = set()
        for px, py in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if not (0 <= px < dim and 0 <= py < dim):
                continue
            graph[(x, y)].add((px, py))

for limit in range(len(corrupted)):
    cx, cy = corrupted[limit]
    graph[(cx, cy)].clear()
    for px, py in [(cx + 1, cy), (cx, cy + 1), (cx - 1, cy), (cx, cy - 1)]:
        if not (0 <= px < dim and 0 <= py < dim):
            continue
        graph[(px, py)].discard((cx, cy))

    visited = set()
    visited.add((0, 0))
    queue = deque([(0, 0)])
    found = False

    while queue:
        node = queue.popleft()

        for other in graph[node]:
            if other in visited:
                continue

            if other == (dim - 1, dim - 1):
                found = True
                break

            visited.add(other)
            queue.append(other)

        if found:
            break

    if not found:
        print(corrupted[limit])
        break
