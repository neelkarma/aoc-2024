NEXT_TURN = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

obstacles = set()
guard = None, None, None
dim = -1

with open("input.txt") as f:
    for y, line in enumerate(f):
        row = line.rstrip()
        for x, char in enumerate(row):
            if char == "#":
                obstacles.add((x, y))
            elif char in "<>^v":
                guard = x, y, char
        dim = y + 1

def patrol(x, y, d, obstacles, new_obstacle=None):
    if new_obstacle is not None:
        obstacles.add(new_obstacle)

    visited = {(x, y, d),}

    while True:
        nx, ny = x, y

        if d == "^":
            ny -= 1
        elif d == ">":
            nx += 1
        elif d == "v":
            ny += 1
        elif d == "<":
            nx -= 1

        if not (0 <= nx < dim and 0 <= ny < dim):
            break

        if (nx, ny) in obstacles:
            d = NEXT_TURN[d]
        else:
            x, y = nx, ny

        if (x, y, d) in visited:
            return None # infinite loop

        visited.add((x, y, d))

    return set((x, y) for x, y, d in visited)

x, y, d = guard
positions = patrol(x, y, d, obstacles)
count  = 0

for px, py in positions:
    if (px, py) in obstacles or (px, py) == (x, y):
        continue
    if patrol(x, y, d, obstacles.copy(), (px, py)) is None:
        count += 1

print(count)
