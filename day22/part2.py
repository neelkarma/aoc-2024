from collections import defaultdict

nums = []
with open("input.txt") as f:
    nums = [int(line.rstrip()) for line in f]

gains = defaultdict(int)

for secret in nums:
    seen = set()
    changes = []
    prev_price = secret % 10

    for _ in range(2000):
        secret = (secret ^ (secret << 6)) & 16777215
        secret = (secret ^ (secret >> 5)) & 16777215
        secret = (secret ^ (secret << 11)) & 16777215

        price = secret % 10

        if len(changes) == 4:
            changes.pop(0)
            changes.append(price - prev_price)
            changeset = tuple(changes)
            if changeset not in seen:
                gains[changeset] += price
                seen.add(changeset)
        elif len(changes) < 4:
            changes.append(price - prev_price)

        prev_price = price

print(max(gains.values()))
