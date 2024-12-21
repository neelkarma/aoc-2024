from collections import deque


def read_input(fname: str):
    walls = set()
    xi, yi, xf, yf = -1, -1, -1, -1
    dim = 0

    with open("input.txt") as f:
        for y, line in enumerate(f):
            for x, cell in enumerate(line.rstrip()):
                match cell:
                    case "#":
                        walls.add((x, y))
                    case "S":
                        xi, yi = x, y
                    case "E":
                        xf, yf = x, y
            dim = y + 1

    return walls, xi, yi, xf, yf, dim


def find_dists(start, walls):
    dists = {}
    dists[start] = 0
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for px, py in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (px, py) in walls or (px, py) in dists:
                continue
            dists[(px, py)] = dists[(x, y)] + 1
            queue.append((px, py))

    return dists


def generate_cheat_times(max_cheat_time, dists_from_start, dists_from_end, walls, dim):
    for sy in range(dim):
        for sx in range(dim):
            if (sx, sy) in walls:
                continue

            for ey in range(sy - max_cheat_time, sy + max_cheat_time + 1):
                if not (0 <= ey < dim):
                    continue

                breadth = max_cheat_time - abs(ey - sy)
                for ex in range(sx - breadth, sx + breadth + 1):
                    if not (0 <= ex < dim):
                        continue
                    if (ex, ey) in walls:
                        continue

                    cheat_time = abs(ey - sy) + abs(ex - sx)
                    pot_time = (
                        dists_from_start[(sx, sy)]
                        + cheat_time
                        + dists_from_end[(ex, ey)]
                    )
                    yield pot_time
