stones = []
with open("input.txt") as f:
    stones = [int(stone) for stone in f.readline().rstrip().split()]

print(stones)
for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue

        stred = str(stone)
        if len(stred) % 2 == 0:
            new_stones.append(int(stred[:len(stred)//2]))
            new_stones.append(int(stred[len(stred) // 2:]))

        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))
