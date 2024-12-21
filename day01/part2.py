from collections import Counter

l1 = []
l2 = []

with open("input.txt") as f:
    for line in f:
        num1, num2 = map(int, line.rstrip().split())
        l1.append(num1)
        l2.append(num2)

l2 = Counter(l2)
total = sum(num * l2.get(num, 0) for num in l1)

print(total)
