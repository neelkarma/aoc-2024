grids = []

with open("example.txt") as f:
    grids = [grid.splitlines() for grid in f.read().split("\n\n")]

locks = []
keys = []

for grid in grids:
    is_key = True
    if grid[0] == "#####":
        is_key = False

    levels = [-1] * 5

    for i in range(1, 7):
        for j in range(5):
            if levels[j] != -1:
                continue

            if is_key and grid[i][j] == "#":
                levels[j] = 6 - i
            elif not is_key and grid[i][j] == ".":
                levels[j] = i - 1

    if is_key:
        keys.append(levels)
    else:
        locks.append(levels)


answer = 0
for lock in locks:
    for key in keys:
        if not any(a + b > 5 for a, b in zip(lock, key)):
            answer += 1

print(answer)
