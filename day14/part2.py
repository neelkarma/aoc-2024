WIDTH = 101
HEIGHT = 103


robots = []
with open("input.txt") as f:
    for line in f:
        left, right = line.rstrip().split()
        x, y = map(int, left[2:].split(","))
        vx, vy = map(int, right[2:].split(","))
        robots.append([x, y, vx, vy])

secs = 0
while True:
    for i, (x, y, vx, vy) in enumerate(robots):
        robots[i][0] += vx
        robots[i][0] %= WIDTH
        robots[i][1] += vy
        robots[i][1] %= HEIGHT
    secs += 1

    # rationale:
    # the christmas tree-shaped configuration is the one which has no overlapping robots.
    # the fact that this works angers me.
    locs = set()
    for x, y, vx, vy in robots:
        if (x, y) in locs:
            break
        locs.add((x, y))
    else:
        print(secs)
        break
