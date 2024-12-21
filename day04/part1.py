grid: list[str] = []
with open("input.txt") as f:
    for line in f:
        grid.append(line.rstrip())
dim = len(grid)

def count_substrs(gen, substr):
    return "".join(list(gen)).count(substr)

def rows():
    for row in grid:
        yield row

def col(x):
    for y in range(dim):
        yield grid[y][x]

def cols():
    for x in range(dim):
        yield col(x)

def upward_diag(start_x, start_y):
    x = start_x
    y = start_y

    while x < dim and y >= 0:
        yield grid[y][x]

        x += 1
        y -= 1

def upward_diags():
    for start_y in range(dim):
        yield upward_diag(0, start_y)

    for start_x in range(1, dim):
        yield upward_diag(start_x, dim - 1)


def downward_diag(start_x, start_y):
    x = start_x
    y = start_y

    while x < dim and y < dim:
        yield grid[y][x]

        x += 1
        y += 1

def downward_diags():
    for start_y in range(dim - 1, -1, -1):
        yield downward_diag(0, start_y)

    for start_x in range(1, dim):
        yield downward_diag(start_x, 0)

count = 0

for callable in [rows, cols, downward_diags, upward_diags]:
    for gen in callable():
        count += count_substrs(gen, "XMAS")
    for gen in callable():
        count += count_substrs(gen, "SAMX")

print(count)
