def viz(x, y, boxes, dim):
    for cy in range(dim):
        row = []
        for cx in range(dim):
            if (cx, cy) in boxes:
                row.append("O")
            elif (cx, cy) in walls:
                row.append("#")
            elif (cx, cy) == (x, y):
                row.append("@")
            else:
                row.append(".")
        print("".join(row))


walls = set()
boxes = set()
x, y = -1, -1
dim = -1

dirs = []

with open("input.txt") as f:
    grid, actions = f.read().split("\n\n")

    grid = grid.split("\n")
    dim = len(grid)

    for cy, line in enumerate(grid):
        for cx, cell in enumerate(line.rstrip()):
            if cell == "O":
                boxes.add((cx, cy))
            elif cell == "#":
                walls.add((cx, cy))
            elif cell == "@":
                x, y = cx, cy

    for line in actions:
        dirs += [char for char in line.rstrip()]

# method:
#
for d in dirs:
    # print("Direction:", d)
    # viz(x, y, boxes, dim)
    # input("...")
    if d == "^":
        if y == 0:
            continue

        if (x, y - 1) not in boxes and (x, y - 1) not in walls:
            y -= 1
            continue

        my = None
        for py in range(y - 1, -1, -1):
            if (x, py) in walls:
                break
            if (x, py) not in boxes:
                my = py
                break

        if my is not None:
            boxes.remove((x, y - 1))
            boxes.add((x, my))
            y -= 1
    elif d == ">":
        if x == dim - 1:
            continue

        if (x + 1, y) not in boxes and (x + 1, y) not in walls:
            x += 1
            continue

        mx = None
        for px in range(x + 1, dim):
            if (px, y) in walls:
                break
            if (px, y) not in boxes:
                mx = px
                break

        if mx is not None:
            boxes.remove((x + 1, y))
            boxes.add((mx, y))
            x += 1

    elif d == "v":
        if y == dim - 1:
            continue
        if (x, y + 1) not in boxes and (x, y + 1) not in walls:
            y += 1
            continue

        my = None
        for py in range(y + 1, dim):
            if (x, py) in walls:
                break
            if (x, py) not in boxes:
                my = py
                break

        if my is not None:
            boxes.remove((x, y + 1))
            boxes.add((x, my))
            y += 1

    elif d == "<":
        if x == 0:
            continue

        if (x - 1, y) not in boxes and (x - 1, y) not in walls:
            x -= 1
            continue

        mx = None
        for px in range(x - 1, -1, -1):
            if (px, y) in walls:
                break
            if (px, y) not in boxes:
                mx = px
                break

        if mx is not None:
            boxes.remove((x - 1, y))
            boxes.add((mx, y))
            x -= 1

answer = sum(100 * by + bx for bx, by in boxes)
print(answer)
