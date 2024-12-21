import math

WIDTH = 101
HEIGHT = 103


robots = []
with open("input.txt") as f:
    for line in f:
        left, right = line.rstrip().split()
        x, y = map(int, left[2:].split(","))
        vx, vy = map(int, right[2:].split(","))
        robots.append([x, y, vx, vy])

secs = 100
for i, (x, y, vx, vy) in enumerate(robots):
    robots[i][0] += vx * secs
    robots[i][0] %= WIDTH
    robots[i][1] += vy * secs
    robots[i][1] %= HEIGHT

q1, q2, q3, q4 = 0, 0, 0, 0

for x, y, vx, vy in robots:
    if 0 <= x < WIDTH // 2:
        if 0 <= y < HEIGHT // 2:
            q1 += 1
        elif math.ceil(HEIGHT / 2) <= y < HEIGHT:
            q4 += 1
    elif math.ceil(WIDTH / 2) <= x < WIDTH:
        if 0 <= y < HEIGHT // 2:
            q2 += 1
        elif math.ceil(HEIGHT / 2) <= y < HEIGHT:
            q3 += 1

answer = q1 * q2 * q3 * q4
print(answer)
