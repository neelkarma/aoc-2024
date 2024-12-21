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

x, y, d = guard
visited = {(x, y),}

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
        continue

    x,y = nx, ny
    visited.add((x, y))

print(len(visited))
