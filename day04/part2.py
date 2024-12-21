grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(line.rstrip())
dim = len(grid)


def check_xmas(x, y):
    return grid[y + 1][x + 1] == "A" and (
        (
            grid[y][x] == "M"
            and grid[y + 2][x] == "M"
            and grid[y + 2][x + 2] == "S"
            and grid[y][x + 2] == "S"
        )
        or (
            grid[y][x] == "S"
            and grid[y + 2][x] == "M"
            and grid[y + 2][x + 2] == "M"
            and grid[y][x + 2] == "S"
        )
        or (
            grid[y][x] == "S"
            and grid[y + 2][x] == "S"
            and grid[y + 2][x + 2] == "M"
            and grid[y][x + 2] == "M"
        )
        or (
            grid[y][x] == "M"
            and grid[y + 2][x] == "S"
            and grid[y + 2][x + 2] == "S"
            and grid[y][x + 2] == "M"
        )
    )


count = 0
for y in range(dim - 2):
    for x in range(dim - 2):
        if check_xmas(x, y):
            count += 1
print(count)
