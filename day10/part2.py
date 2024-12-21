grid = []
with open("input.txt") as f:
    grid = [[int(char) for char in line.rstrip()] for line in f]
dim = len(grid)

trailheads = []
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 0:
            trailheads.append((x, y))

total = 0
for ox, oy in trailheads:
    paths = [[(ox, oy)]]
    rating = 0

    while paths:
        path = paths.pop(0)
        x, y = path[-1]
        last_num = grid[y][x]

        for px, py in [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1)
        ]:
            if not (0 <= px < dim and 0 <= py < dim):
                continue

            if grid[py][px] != last_num + 1:
                continue

            if grid[py][px] == 9:
                rating += 1
                continue

            paths.append(path + [(px, py)])

    total += rating

print(total)
