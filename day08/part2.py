antennae = {}
dim = 0

with open("input.txt") as f:
    for y, line in enumerate(f):
        line = line.rstrip()
        for x, cell in enumerate(line):
            if cell != ".":
                if cell in antennae:
                    antennae[cell].append((x, y))
                else:
                    antennae[cell] = [(x, y)]
        dim = y + 1

antinodes = set()
for coords in antennae.values():
    for i in range(len(coords)):
        x1, y1 = coords[i]
        for j in range(i + 1, len(coords)):
            x2, y2 = coords[j]

            vx, vy = x2 - x1, y2 - y1

            ax, ay = x1, y1
            while 0 <= ax < dim and 0 <= ay < dim:
                antinodes.add((ax, ay))
                ax -= vx
                ay -= vy

            ax, ay = x2, y2
            while 0 <= ax < dim and 0 <= ay < dim:
                antinodes.add((ax, ay))
                ax += vx
                ay += vy

print(len(antinodes))
