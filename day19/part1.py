from collections import deque

patterns: list[str] = []
designs: list[str] = []

with open("example.txt") as f:
    patterns = f.readline().rstrip().split(", ")
    f.readline()
    designs = [line.rstrip() for line in f]

num_possible = 0
for design in designs:
    print(design)
    possible = False
    queue = deque([design])

    while queue:
        # print(len(queue))
        part = queue.pop()
        for pattern in patterns:
            if not part.startswith(pattern):
                continue
            new_part = part[len(pattern) :]
            if len(new_part) == 0:
                possible = True
                break
            queue.append(new_part)
        if possible:
            break

    if possible:
        num_possible += 1

print(num_possible)
