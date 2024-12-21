walls = set()
boxes = set()
x, y = -1, -1
width = -1
height = -1

dirs = []

with open("input.txt") as f:
    grid, actions = f.read().split("\n\n")

    grid = grid.split("\n")
    height = len(grid)
    width = height * 2

    for cy, line in enumerate(grid):
        for cx, cell in enumerate(line.rstrip()):
            if cell == "O":
                boxes.add((cx * 2, cy))
            elif cell == "#":
                walls.add((cx * 2, cy))
                walls.add((cx * 2 + 1, cy))
            elif cell == "@":
                x, y = cx * 2, cy

    for line in actions:
        for char in line.rstrip():
            dirs.append(char)

for d in dirs:
    if d == "^":
        if (x, y - 1) in walls:
            continue
        if (x, y - 1) not in boxes and (x - 1, y - 1) not in boxes:
            y -= 1
            continue

        can_move = True
        affected = set()
        queue = []

        if (x, y - 1) in boxes:
            queue.append((x, y - 1))
        elif (x - 1, y - 1) in boxes:
            queue.append((x - 1, y - 1))

        while queue:
            bx, by = queue.pop(0)
            affected.add((bx, by))

            if any(
                (pwx, pwy) in walls for pwx, pwy in [(bx, by - 1), (bx + 1, by - 1)]
            ):
                can_move = False
                break

            for pbx, pby in [(bx - 1, by - 1), (bx, by - 1), (bx + 1, by - 1)]:
                if (pbx, pby) in boxes:
                    queue.append((pbx, pby))

        if not can_move:
            continue

        for bx, by in affected:
            boxes.remove((bx, by))
        for bx, by in affected:
            boxes.add((bx, by - 1))
        y -= 1

    elif d == ">":
        if (x + 1, y) in walls:
            continue

        if (x + 1, y) not in boxes:
            x += 1
            continue

        can_move = True
        affected = set()

        px = x + 1
        while px < width:
            if (px, y) in boxes:
                affected.add((px, y))
            elif (px, y) in walls:
                can_move = False
                break
            else:
                break
            px += 2

        if not can_move:
            continue

        for bx, by in affected:
            boxes.remove((bx, by))
        for bx, by in affected:
            boxes.add((bx + 1, by))
        x += 1

    elif d == "v":
        if (x, y + 1) in walls:
            continue

        if (x, y + 1) not in boxes and (x - 1, y + 1) not in boxes:
            y += 1
            continue

        can_move = True
        affected = set()
        queue = []

        if (x, y + 1) in boxes:
            queue.append((x, y + 1))
        elif (x - 1, y + 1) in boxes:
            queue.append((x - 1, y + 1))

        while queue:
            bx, by = queue.pop(0)
            affected.add((bx, by))

            if any(
                (pwx, pwy) in walls for pwx, pwy in [(bx, by + 1), (bx + 1, by + 1)]
            ):
                can_move = False
                break

            for pbx, pby in [(bx - 1, by + 1), (bx, by + 1), (bx + 1, by + 1)]:
                if (pbx, pby) in boxes:
                    queue.append((pbx, pby))

        if not can_move:
            continue

        for bx, by in affected:
            boxes.remove((bx, by))
        for bx, by in affected:
            boxes.add((bx, by + 1))
        y += 1

    elif d == "<":
        if (x - 1, y) in walls:
            continue
        if (x - 2, y) not in boxes:
            x -= 1
            continue

        can_move = True
        affected = set()

        px = x - 2
        while px >= 0:
            if (px, y) in boxes:
                affected.add((px, y))
            elif (px, y) in walls:
                if (px + 1, y) in walls:
                    can_move = False
                break
            else:
                break
            px -= 2

        if not can_move:
            continue

        for bx, by in affected:
            boxes.remove((bx, by))
        for bx, by in affected:
            boxes.add((bx - 1, by))
        x -= 1


answer = sum(100 * by + bx for bx, by in boxes)
print(answer)
