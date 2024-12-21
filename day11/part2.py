from collections import Counter, defaultdict


def op(stone):
    if stone == 0:
        return [1]

    stred = str(stone)
    if len(stred) % 2 == 0:
        left = int(stred[:len(stred)//2])
        right =  int(stred[len(stred) // 2:])
        return [left, right]
    else:
        return [stone * 2024]


stones = {}
with open("input.txt") as f:
    stones = dict(Counter(int(stone) for stone in f.readline().rstrip().split()))

print(stones)
for i in range(75):
    new_stones = defaultdict(int)
    for stone, n in stones.items():
        for new_stone in op(stone):
            new_stones[new_stone] += n
    stones = new_stones

print(sum(stones.values()))
