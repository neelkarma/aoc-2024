from functools import cache

patterns: list[str] = []
designs: list[str] = []

with open("example.txt") as f:
    patterns = f.readline().rstrip().split(", ")
    f.readline()
    designs = [line.rstrip() for line in f]


@cache
def find_num_arrangements(part):
    num_possible = 0
    for pattern in patterns:
        if not part.startswith(pattern):
            continue
        new_part = part[len(pattern) :]
        if len(new_part) == 0:
            num_possible += 1
        else:
            num_possible += find_num_arrangements(new_part)
    return num_possible


answer = sum(map(find_num_arrangements, designs))
print(answer)
